import sys
from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_resource import MetricResource
from datadog_api_client.v2.model.metric_series import MetricSeries

if len(sys.argv) > 1:
    fltValue = float(sys.argv[1])
else:
    fltValue = 0.0

body = MetricPayload(
    series = [
        MetricSeries(
            metric = "kano_NodeRED_value",
            type = MetricIntakeType.UNSPECIFIED,
            points = [
                MetricPoint(
                    timestamp = int(datetime.now().timestamp()),
                    value = fltValue,
                ),
            ],
            resources = [
                MetricResource(
                    name = "Node-RED",
                    type = "host",
                ),
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_metrics(body=body)

    print(response)
