import time
import re


class GranularityProcessor(object):
    def __init__(self, granularity):
        self.granularity = granularity

    def granularity_in_minutes(self):
        if self.granularity == 'minute':
            return 60

        if self.granularity == 'hour':
            return 60*60

        if self.granularity == 'three_hour':
            return 3*60*60

        if self.granularity == 'six_hour':
            return 6*60*60

        if self.granularity == 'twelve_hour':
            return 12*60*60

        if self.granularity == 'day':
            return 24*60*60

        if self.granularity == 'week':
            return 7*24*60*60

        if self.granularity == 'month':
            return 30*24*60*60

    def process(self, data):
        granularity_in_minutes = self.granularity_in_minutes()

        grouped_data = {}

        for item in data:
            timestamp = item['x']
            slot = long(timestamp - (timestamp % (granularity_in_minutes * 1000)))
            if slot not in grouped_data:
                grouped_data[slot] = []

            grouped_data[slot].append(item)


        agreggated_data = []
        for timestamp, data in grouped_data.iteritems():
            sum = 0
            for item in data:
                sum += item['y']

            processed_item = {
                "x": timestamp,
                "y": sum
            }

            agreggated_data.append(processed_item)

        return sorted(agreggated_data, key=lambda k: k['x'])



class MetricDataProvider(object):
    def __init__(self, metrics_configuration, mysql_connector):
        self.metrics_configuration = metrics_configuration
        self.mysql_connector = mysql_connector

    def get_series(self, chart_properties):
        metric_name = chart_properties['metric']
        summary_table = self.metrics_configuration.get_summary_table(metric_name)
        granularity_processor = GranularityProcessor(chart_properties['granularity'])

        series = []

        initial_timestamp = self.__convert_from_text_to_timestamp(chart_properties['from'])
        final_timestamp = self.__convert_from_text_to_timestamp(chart_properties['to'])
        series.append(self.get_main_serie(metric_name, summary_table, initial_timestamp, final_timestamp, granularity_processor))

        compare_field = chart_properties['compare_to']
        if compare_field:
            diff_time = final_timestamp - initial_timestamp
            initial_timestamp = self.__convert_from_text_to_timestamp(compare_field)
            final_timestamp = initial_timestamp + diff_time
            series.append(self.get_compare_serie(metric_name, summary_table, initial_timestamp, final_timestamp, granularity_processor))

        return series

    def get_data(self, summary_table, initial_timestamp, final_timestamp):
        query = """SELECT time, value FROM `{table_name}` WHERE time > {initial_timestamp} AND time <= {final_timestamp};""".format(
            table_name=summary_table,
            initial_timestamp=initial_timestamp,
            final_timestamp=final_timestamp
        )

        cur = self.mysql_connector.cursor()
        cur.execute(query)
        self.mysql_connector.commit()

        result_data = []
        for (item_time, item_value) in cur.fetchall():
            result_item = {
                "x": item_time*1000,
                "y": item_value
            }

            result_data.append(result_item)

        return result_data

    def get_main_serie(self, metric_name, summary_table, initial_timestamp, final_timestamp, granularity_processor):
        data = self.get_data(summary_table, initial_timestamp, final_timestamp)

        return {
            "metric": metric_name,
            "name": "Today - {}".format(metric_name),
            "app": "Mailtrack",
            "unit": "Users",
            "dimensions": [],
            "turboThreshold": 0,
            "data": granularity_processor.process(data),
            "serieType": "datetime",
            "transformations": []
        }

    def get_compare_serie(self, metric_name, summary_table, initial_timestamp, final_timestamp, granularity_processor):
        data = self.get_data(summary_table, initial_timestamp, final_timestamp)
        offset = final_timestamp-initial_timestamp

        data_with_offset = self.__shift_data(data, offset)
        return {
            "metric": metric_name,
            "name": "Yesterday - {} [cmp]".format(metric_name),
            "app": "Mailtrack",
            "unit": "Users",
            "dimensions": [],
            "turboThreshold": 0,
            "data": granularity_processor.process(data_with_offset),
            "serieType": "datetime",
            "transformations": []
        }

    def __convert_from_text_to_timestamp(self, text_date):
        current_timestamp = int(time.time())

        if text_date == 'now':
            return current_timestamp

        result = re.match(r'^\-(\d+)\s*(\w+)$', text_date)

        units = result.group(2)
        value = int(result.group(1))

        if units == 'weeks':
            seconds = 7*24*60*60
        elif units == 'days':
            seconds = 24*60*60
        elif units == 'hours':
            seconds = 24*60
        else:
            seconds = 24*60*60
            print 'units {} are not valid'.format(units)

        return current_timestamp - value * seconds

    def __shift_data(self, data, offset_in_seconds):
        result_data = []

        for item in data:
            result_item = {
                "x": item['x']+(offset_in_seconds*1000),
                "y": item['y']
            }

            result_data.append(result_item)

        return result_data


class ChartPropertiesProvider(object):
    def get_properties(self, chart_id):
        if chart_id == 1:
            return {
                "from": '-1 days',
                "to": "now",
                "compare_to": '-7 days',
                "granularity": 'hour',
                "chart_type": 'line',
                "application": '',
                "dimension": '',
                "metric": 'email.open',
                "platform": 'web'
            }

        if chart_id == 2:
            return {
                "from": '-1 days',
                "to": "now",
                "compare_to": '',
                "granularity": 'hour',
                "chart_type": 'line',
                "application": '',
                "dimension": '',
                "metric": 'user.signup',
                "platform": 'web'
            }

        if chart_id == 3:
            return {
                "from": '-1 days',
                "to": "now",
                "compare_to": '-2 days',
                "granularity": 'hour',
                "chart_type": 'line',
                "application": '',
                "dimension": '',
                "metric": 'email.track.created',
                "platform": 'web'
            }

        if chart_id == 4:
            return {
                "from": '-1 days',
                "to": "now",
                "compare_to": '',
                "granularity": 'hour',
                "chart_type": 'line',
                "application": '',
                "dimension": '',
                "metric": 'crx.uninstall',
                "platform": 'web'
            }

        if chart_id == 5:
            return {
                "from": '-1 days',
                "to": "now",
                "compare_to": '',
                "granularity": 'hour',
                "chart_type": 'line',
                "application": '',
                "dimension": '',
                "metric": 'user.acquired',
                "platform": 'web'
            }

        if chart_id == 6:
            return {
                "from": '-1 days',
                "to": "now",
                "compare_to": '-2 days',
                "granularity": 'hour',
                "chart_type": 'line',
                "application": '',
                "dimension": '',
                "metric": 'user.info',
                "platform": 'web'
            }
