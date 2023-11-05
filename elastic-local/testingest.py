from datetime import datetime
from elasticsearch import Elasticsearch, RequestsHttpConnection

# Connect to Elasticsearch running on your local machine
es = Elasticsearch(hosts=["https://localhost:9200"],    connection_class=RequestsHttpConnection,
    use_ssl=True,
    verify_certs=False  # Set to True if you have proper SSL certificates installed
)

# Index name and document type
index_name = "your-index-name"

# Example data to be indexed
data = {
    "timestamp": datetime.now(),
    "message": "Hello, Elasticsearch!"
}

# Index the data
es.index(index=index_name, body=data)

# Refresh the index (optional)
es.indices.refresh(index=index_name)

# Search for the indexed document
search_results = es.search(index=index_name, body={"query": {"match_all": {}}})

# Print the search results
for hit in search_results["hits"]["hits"]:
    print(hit["_source"])