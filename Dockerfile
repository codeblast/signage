#
# Dockerfile for signage web app.
#

# Pull base image.
FROM ubuntu:16.04

# Update sources.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade
  
# Install Ubuntu basics.
RUN \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl dialog git htop man net-tools unzip vim wget

# Install Python.
RUN \
  add-apt-repository ppa:jonathonf/python-3.6 && \
  apt-get update && \
  apt-get install -y python-software-properties python3.6 python3-pip

RUN pip3 install --upgrade pip

# Clear apt-get cache.
RUN rm -rf /var/lib/apt/lists/*

# Add the source code to the image.
ADD . /app/

# Set environment variables.
ENV HOME /app

# Define working directory.
WORKDIR /app

# Install Flask.
RUN pip3 install -r requirements.txt

# Run the Flask server.
EXPOSE 8080
CMD ["python3", "/app/app.py"]
