#
# Dockerfile for the signage app's API layer.
#

# Pull base image.
FROM ubuntu:16.04

# Disable interactive mode to avoid some errors in apt-get.
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Update package sources.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y software-properties-common && \
  apt-get install -y python-software-properties && \
  add-apt-repository ppa:jonathonf/python-3.6 && \
  apt-get update && \
  apt-get -y upgrade
  
# Install Ubuntu basics.
RUN \
  apt-get install -y build-essential && \
  apt-get install -y byobu curl dialog git htop man net-tools unzip vim wget

# Install Python.
RUN \
  apt-get install -y python3.6 python3-pip

RUN pip3 install --upgrade pip

# Clear apt-get cache.
RUN \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add the source code to the image.
ADD . /api

# Set environment variables.
ENV HOME /api

# Define working directory.
WORKDIR /api

# Install Flask.
RUN pip3 install -r requirements.txt

# Run the Flask server.
EXPOSE 8080
CMD ["python3", "/api/app.py"]
