FROM ubuntu:22.04

# LABEL name=testparser

# install java and logstash
RUN apt-get update -y && \
    apt-get install gnupg2 -y &&\
    apt-get install wget -y && \
    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    apt-get install apt-transport-https -y && \
    echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-8.x.list && \
    apt-get update -y && \
    apt-get install default-jre -y && \
    apt-get install logstash -y

# install extras and upgrade
RUN apt-get install vim -y
    # apt-get upgrade


COPY pipeline/hi.conf /etc/logstash/conf.d/

ENV PATH /usr/share/logstash/bin:$PATH


# test es access
# possibly generate/verify api key
# curl -k -X GET -H "Authorization: ApiKey Qk5ETVo0UUJfOEZqaXBEUURNMEk6b01nNGpnSnFUYUtXOU1VbGJHY19KQQ==" https://192.168.1.38:9200/_cat/
