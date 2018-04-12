#!/usr/bin/env bash

docker build . -t signage

docker run -it -p 8080:8080 signage
