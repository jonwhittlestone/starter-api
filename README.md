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

#### Run the container tests

```bash
make rebuild-d; \
docker-compose exec web-test pytest tests -x -o log_cli=true
```

#### Container Development aka. start a-fresh
```
make rebuild
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


#### Alembic Migrations
- https://testdriven.io/blog/fastapi-sqlmodel/
- https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic
