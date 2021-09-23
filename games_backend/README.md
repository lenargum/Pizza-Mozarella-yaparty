# Y.Party games collection backend

## Run locally

```
cd games_backend/app
uvicorn main:app --reload
```

## Run in docker

```
# Build games container
cd games_backend
docker build -t games_backend .

# Run container
docker run -d --name games_backend_main -p 8000:80 games_backend
```

## Links

Swagger: [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)
