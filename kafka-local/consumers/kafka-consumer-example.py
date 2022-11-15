from kafka import KafkaConsumer
consumer = KafkaConsumer('dynamic-topic-create', group_id='v1', bootstrap_servers='localhost:9092')
for msg in consumer:
    print (msg)