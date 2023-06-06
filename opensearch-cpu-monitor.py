import subprocess
import datetime
from elasticsearch import Elasticsearch

# AWS OpenSearch settings
opensearch_endpoint = '<your-opensearch-endpoint>'
index_name = '<your-index-name>'

def get_cpu_stress():
    # Run the 'stress' command to generate CPU stress
    subprocess.run(['stress', '--cpu', '1', '--timeout', '10s'])

    # Fetch CPU stress metrics
    process = subprocess.run(['top', '-bn', '1'], capture_output=True, text=True)
    output = process.stdout

    # Parse the output to extract CPU stress metrics
    cpu_metrics = {}
    for line in output.split('\n'):
        if 'Cpu(s)' in line:
            fields = line.split(',')
            for field in fields:
                if 'id' in field:
                    cpu_metrics['idle'] = float(field.split('%')[0])
                elif 'us' in field:
                    try:
                        cpu_metrics['user'] = float(field.split('%')[0])
                    except ValueError:
                        cpu_metrics['user'] = 0.0
                elif 'sy' in field:
                    try:
                        cpu_metrics['system'] = float(field.split('%')[0])
                    except ValueError:
                        cpu_metrics['system'] = 0.0
                elif 'ni' in field:
                    try:
                        cpu_metrics['nice'] = float(field.split('%')[0])
                    except ValueError:
                        cpu_metrics['nice'] = 0.0

    return cpu_metrics

def index_to_opensearch(metrics):
    # Create an Elasticsearch client
    es = Elasticsearch(opensearch_endpoint)

    # Prepare index data
    timestamp = datetime.datetime.now().isoformat()
    index_data = {
        '@timestamp': timestamp,
        'idle': metrics['idle'],
        'user': metrics['user'],
        'system': metrics['system'],
        'nice': metrics['nice']
    }

    # Index data into OpenSearch
    es.index(index=index_name, body=index_data)

def main():
    cpu_metrics = get_cpu_stress()
    index_to_opensearch(cpu_metrics)

if __name__ == '__main__':
    main()
