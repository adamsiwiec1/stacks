from elasticsearch import Elasticsearch


client = Elasticsearch(
    "https://localhost:9200/",
    api_key="bUktTllvUUJuVkl0Wkw3R25ySWY6QkZSY2JVcjZUNy1LVGdVSFE2bVI2dw==",
    verify_certs=False
)

client.indices.create(index='test-index-2', ignore=400)

