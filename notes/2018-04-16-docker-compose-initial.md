# Introducing docker-compose

Creating a separate Docker image for the Postgres database:
`/db/Dockerfile`.

My goal is to try to keep each root-level API service
separate. The database server is currently one such
root-level API, but in the future we may have multiple
root-level APis each with their own separate database.

Created the `docker-compose.yml` configuration file to link
the 2 current Docker images together:

1. API layer: /Dockerfile
2. Db layer: /db/Dockerfile

The `docker-compose.yml` file allows us to use the
`docker-compose` command to build or run *all* Docker
containers simultaneously. We can build and start everything
to run the web app with just one line:

```bash
docker-compose up
```

# Shell commands

Some random commands from my shell history that seemed
like I may need to refer back to this later. ?????

```bash
docker-compose build
docker-compose up
docker-compose build && docker-compose down && docker-compose up
docker-compose rm -fs

docker exec -it signage_db_1 bash

docker build db/ -t db && docker run -it db bash
psql -d signage -U signage -W
psql -d signage -U signage -W -f /docker-entrypoint-initdb.d/01-create-checkin-db.sql
ls /docker-entrypoint-initdb.d/
```

# BLOCKING ISSUE - USER FOO DOES NOT WORK:

As an experiment, I added a script `01-create-checkin-db.sql`
under `/db/init/`. The Dockerfile seems to pick it up,
but I can't get any evidence yet that this script actually
got executed.

Not a big deal for now, but I need to figure out why
scripts under the 'init' folder doesn't just work automatically.

Issue: Can't connect with user `foo` which we try to create in
`/db/init/01-create-checkin-db.sql`:

```bash
psql -U foo -d signage -W
Password for user foo: foo_pwd
psql: could not connect to server: No such file or directory
	Is the server running locally and accepting
	connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?
```

Oh, I figured it out! The docker-compose.yml file had the wrong
image name for the db instance, so it used the base postgres
image instead of mine with the /init directory.

# TODO

Some obvious next steps include:

1. Fix the postgres port and map it appropriately
2. Move the API Dockerfile underneath /api
3. Add additional Docker images for `/admin` and `/pages`,
   refactor `/api` to split out the static stuff to `/pages` or `/static`.
4. Document how to make this work on macOS: all the Docker stuff we have
   means I've only run the code in Linux via Docker so far. So, I still
   have to figure out how to do the same in native MacOS.
5. Ditto for Windows.
