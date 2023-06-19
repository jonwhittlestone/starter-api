# starter-api

## Usage
```bash
make up-build
```

Run the command above and then visit: http://localhost:8004 

## Debugging: Debugging FastAPI using vscode

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
- [x] Postgres service, SQLModel + SQLAlchemy, Alembic migrations
- [ ] Poetry, Dynaconf
- [ ] Containerised tests
- [ ] Github Action to run tests
- [ ] Production deployment
- [ ] Tag this repo.
```

<!-- 
```
- [ ] Simple React Typescript Frontend
- [ ] Okta auth
- [ ] Rename starter-full-stack-with-sensible-defaults

```
-->

## Snippets & Resources

### Check Provisioning
- `docker-compose exec db psql --username=postgres --dbname=starter_db_dev`
- `\dt`

### Insert a record
- `make up`; 
- `curl -d '{"name":"Blood Sugar Sex Magik", "artist":"RHCP", "year":"1991"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8004/albums`

### Start a-fresh
- `make down-v; make up-build`

### Alembic Migrations
- https://testdriven.io/blog/fastapi-sqlmodel/
- https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic
