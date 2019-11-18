#!/bin/bash

ETH0=$(ip a | grep eth0 | wc -l)

while [ $ETH0 -eq 0 ]
do
  echo "waiting ... "
  sleep 2
  ETH0=$(ip a | grep eth0 | wc -l)
done

sawtooth-rest-api -C tcp://10.0.0.1:4004 --bind 10.0.0.4:8008