# Bookstore
An online Bookstore API built with FastAPI

## Getting Started

#### Requirements:

- docker
- docker-compose

#### Startup:
```commandline
docker-compose up -d --build
```

#### Apply migrations:
```commandline
docker-compose exec web alembic upgrade head
```

#### Inital Data
```
docker-compose exec web python /code/app/initial_data.py
```

