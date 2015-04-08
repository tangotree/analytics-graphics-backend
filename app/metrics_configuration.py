import yaml


class MetricsConfiguration(object):
    def __init__(self, config_file):
        self.config_file = config_file

        with open(self.config_file, 'r') as f:
            self.config = yaml.load(f)

    def get_summary_table(self, metric_name):
        try:
            summary_table = self.config['metrics'][metric_name]['summary_table']

            if summary_table is None:
                summary_table = 'summary_table_' + metric_name
        except Exception as e:
            return None

        return summary_table