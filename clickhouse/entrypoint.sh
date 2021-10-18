#!/bin/bash

echo "RATATA!!!"
sleep 5
echo "TADA!!!"
dbmate --url "clickhouse://clickhouse-server:10000" up
