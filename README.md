# starter-api

## Usage
```bash
make up-build
```

Run the command above and then visit: http://127.0.0.1:8004 


### Run the container 

## Debugging: Debugging FastAPI using VSCode

1. Run this:
    ```bash
    make up-build
    ```

2. In vscode add a breakpoint

3. Run the debugger (F5)

4. Visit: http://127.0.0.1:8004 

5. The vscode debugger will pause execution at your breakpoint.

## Features

```
- [x] Dockerised w/debug
- [x] Postgres service / SQLModel + SQLAlchemy / Alembic migrations
- [x] Poetry, Dynaconf
- [x] Containerised tests
- [ ] Github Action to run tests
    - https://earthly.dev/blog/github-actions-and-docker/
    - https://testdriven.io/blog/deploying-django-to-linode-with-docker-and-github-actions/
- [ ] FastAPI repositories, schemas / logging / cleanup and mocked tests
- [ ] Production deployment
- [ ] Pre-commit / manage.py / migrations
- [ ] Tag this repo and release
```

<!-- 
```
- [ ] Simple React Typescript Frontend
- [ ] Okta auth
- [ ] Rename starter-full-stack-with-sensible-defaults

```
-->

## Snippets & Resources


#### Container Development aka. start a-fresh
```
make rebuild
```
#### Run the container tests

Warning: The `make rebuild-d` command will remove your postgres volume. 

```bash
make rebuild-d; \
docker-compose exec web-test tests -x -o log_cli=true
```

#### Check DB Provisioning
```bash
docker-compose exec db psql --username=postgres --dbname=starter_db_dev

\dt
```
#### Insert a record
```bash
curl -d '{"name":"Blood Sugar Sex Magik", "artist":"RHCP", "year":"1991"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8004/albums
```

#### Docker: Build, Tag and Push (GitHub packages)
```bash
docker build -f Dockerfile -t ghcr.io/jonwhittlestone/starter-api/web:la
test .

docker build -f Dockerfile.test -t ghcr.io/jonwhittlestone/starter-api/web-test:latest .

docker login ghcr.io -u jonwhittlestone -p changeme

docker push ghcr.io/jonwhittlestone/starter-api/web:latest

docker push ghcr.io/jonwhittlestone/starter-api/web-test:latest

```
Then check:

https://github.com/jonwhittlestone?tab=packages


#### Alembic Migrations
- https://testdriven.io/blog/fastapi-sqlmodel/
- https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic
