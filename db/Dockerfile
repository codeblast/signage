#
# Dockerfile for the signage app's database layer.
#
# TODO: We're using Postgres for now, but remember this may change!
# Or, we may decide to support alternate db sources too, like cloud storage...
#

# Base image from: https://hub.docker.com/_/postgres/
FROM postgres:10.3-alpine

# Set Postgres environment vars to make logging in easier
ENV POSTGRES_DB signage
ENV POSTGRES_PASSWORD pwd
ENV POSTGRES_USER signage

# Add .sql scripts to be executed on the database
ADD init/* /docker-entrypoint-initdb.d/
