#
# Dockerfile for signage web app
#

# Pull base image.
FROM ubuntu:14.04

# Update sources.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade

# Install ubuntu basics.
RUN \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  rm -rf /var/lib/apt/lists/*

# Install Python.
RUN add-apt-repository ppa:jonathonf/python-3.6 && \
  apt-get update && \
  apt-get install -y python3.6 python3.6-dev python3-pip && \
  rm -rf /var/lib/apt/lists/*

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
