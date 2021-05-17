README

# Python Use FastAPI and Gino Template

* Install `web_fastapi`

```bat
pip install -e .[web,db,testing]
```
* Install Docker PostgreSql DataBase

```
docker run --rm --name postgres_db -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user -e POSTGRES_DB=gino_db -d postgres
```

* Use alembic to start database migration

```bat
alembic revision --autogenerate -m 'add users table'
alembic upgrade head
```

* Run Server

```bat
uvicorn web_fastapi.asgi:app
RO 
.\run_win.bat
```

* Start Google Chrome open url http://localhost:8000/docs.