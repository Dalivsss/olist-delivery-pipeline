from google.cloud import bigquery

# Connect using the key from GOOGLE_APPLICATION_CREDENTIALS
client = bigquery.Client(project="olist-delivery-pipeline")

# Run the simplest possible query
result = client.query("SELECT 1 AS connection_ok").result()

for row in result:
    print(f"Connected to BigQuery! Query returned: {row.connection_ok}")