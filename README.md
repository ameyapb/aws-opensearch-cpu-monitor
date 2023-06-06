**OpenSearch CPU Monitor**

This script allows you to monitor CPU stress and index the metrics into an AWS OpenSearch domain. It utilizes the stress command to generate CPU stress and retrieves the CPU stress metrics using the top command. The metrics are then indexed into an OpenSearch domain using the Elasticsearch Python client.

**Prerequisites**

--> Python 3.x.
--> stress command (install using sudo apt install stress).
--> Elasticsearch Python client (install using pip install elasticsearch).

**Configuration**

--> Before running the script, make sure to update the following variables:
--> opensearch_endpoint: Replace with the endpoint URL of your AWS OpenSearch domain.
--> index_name: Replace with the name of the index where you want to store the metrics.

**Usage**

1. Clone this repository to your local machine.
2. Install the prerequisites mentioned in the "Prerequisites" section.
3. Update the configuration variables in the script as mentioned in the "Configuration" section.
4. Run the script using the command python cpu_monitor.py.
