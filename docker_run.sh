#!/usr/bin/env bash

docker-compose down
docker-compose rm -fs
docker-compose build && docker-compose up
