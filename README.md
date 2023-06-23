# starter-api
![Continuous Integration](https://github.com/jonwhittlestone/starter-api/workflows/Continuous%20Integration/badge.svg)

## Usage
```bash
make up-build
```

Run the command above and then visit: http://127.0.0.1:8004 


> See [snippets-resources.md](snippets-resources.md) for handy snippets and resources.


## Debug FastAPI using VSCode

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
- [x] Github Action to run tests
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
