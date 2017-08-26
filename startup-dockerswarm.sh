#!/bin/bash

# create Consul
docker run --restart=always  -d -p 8500:8500 --name=consul progrium/consul -server -bootstrap

sleep 10
# the manager which provides the interface to Docker Swarm:
HUB_LOCAL_IP=$(ip route get 8.8.8.8 | awk 'NR==1 {print $NF}')
docker run --restart=always  -d -p 4000:4000 swarm manage -H :4000 --replication --advertise $HUB_LOCAL_IP:4000 consul://$HUB_LOCAL_IP:8500
