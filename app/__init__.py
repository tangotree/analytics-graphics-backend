import os
from app.metrics_configuration import MetricsConfiguration
from tornado import web
import json
import MySQLdb
from app.data_providers import MetricDataProvider
from app.data_providers import ChartPropertiesProvider


class ApiHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def initialize(self, data_provider, chart_properties_provider):
        self.metrics_data_provider = data_provider
        self.chart_properties_provider = chart_properties_provider

    def get(self, *args):
        self.content_type = 'application/json'

        arguments = self.request.arguments

        if 'chartId' in arguments:
            chart_id = int(arguments['chartId'][0])
        else:
            chart_id = 1

        chart_properties = self.chart_properties_provider.get_properties(chart_id)

        response_data = {
            "title": "Active Users Today vs Yesterday",
            "timezone": "Europe\/Madrid",
            "timezone_offset": 3600,
            "legend_enabled": True,
            "series": self.metrics_data_provider.get_series(chart_properties),
            "flags": [],
            "transformations": []
        }

        response = json.dumps(response_data)
        self.write(response)

    @web.asynchronous
    def post(self):
        pass


class CustomBuilderHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def initialize(self, data_provider):
        self.metrics_data_provider = data_provider

    def get(self, *args, **kwargs):
        self.content_type = 'application/json'

        arguments = self.request.arguments
        query_data = arguments.get('query')[0]
        chart_properties = json.loads(query_data)

        response_data = {
            "title": "Active Users Today vs Yesterday",
            "timezone": "Europe\/Madrid",
            "timezone_offset": 3600,
            "legend_enabled": True,
            "series": self.metrics_data_provider.get_series(chart_properties),
            "flags": [],
            "transformations": []
        }

        response = json.dumps(response_data)
        self.write(response)


def configure_app(config):
    file_directory = os.path.dirname(os.path.abspath(__file__))
    metrics_config_file = os.path.join(file_directory, '../data/metrics.yml')
    metrics_configuration = MetricsConfiguration(metrics_config_file)

    database_configuration = config['database']
    mysql_connector = MySQLdb.connect(**database_configuration) # name of the data base

    data_provider = MetricDataProvider(metrics_configuration, mysql_connector)
    properties_provider = ChartPropertiesProvider()

    app = web.Application([
        (r'/api/builder$', CustomBuilderHandler, dict(data_provider=data_provider)),
        (r'/api$', ApiHandler, dict(data_provider=data_provider, chart_properties_provider=properties_provider)),
        ],
        debug=config['debug']
    )

    return app
