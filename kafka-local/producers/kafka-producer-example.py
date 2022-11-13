from kafka import KafkaProducer
from kafka.errors import KafkaError

# https://kafka-python.readthedocs.io/en/master/


producer = KafkaProducer(bootstrap_servers='localhost:9092')
# for _ in range(100):
future = producer.send('dynamic-topic-create', b'dynamic bytes')
# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)