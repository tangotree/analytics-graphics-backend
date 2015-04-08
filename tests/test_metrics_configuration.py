import os
from unittest import TestCase
from app.metrics_configuration import MetricsConfiguration


class MetricsConfigurationTestCase(TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.configuration = MetricsConfiguration(os.path.join(path, 'fixtures/metrics.yml'))

    def test_get_summary_table_when_specified(self):
        self.assertEquals(self.configuration.get_summary_table('my_metric'), "summary_table_email.open")

    def test_get_summary_table_when_not_specified(self):
        self.assertEquals(self.configuration.get_summary_table('other_metric'), "summary_other_metric")

    def test_get_summary_table_when_inexistent_metric_returns_none(self):
        self.assertIsNone(self.configuration.get_summary_table('non_existent_metric'))
