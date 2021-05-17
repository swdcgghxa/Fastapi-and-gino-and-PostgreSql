:: --reload  --log-level=debug
set str=("OpenApi => http://127.0.0.1:8000/docs")
echo %str%
uvicorn web_fastapi.asgi:app