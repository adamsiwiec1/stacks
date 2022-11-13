kafka-topics --bootstrap-server localhost:9092 --topic first_topic --create --partitions 3 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --list



# send/recieve from console

1. send 
```
kafka-console-producer --broker-list localhost:9092 --topic test-topic
```
2. recieve
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic --from-beginning
```
or, if you'd like historical data add `--from-beginning`