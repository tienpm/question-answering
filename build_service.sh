#!/bin/bash

exe_path=$(pwd)
echo $exe_path

docker build -t elasticsearch -f $exe_path/docker/elasticsearch/ . --mount