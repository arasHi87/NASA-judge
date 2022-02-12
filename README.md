# NASA judge

A RESTful API service for NASA judge, use to build docker container and score.

![Integration](https://github.com/DarkbordermanTemplate/fastapi/workflows/Integration/badge.svg)

## Development

### Prerequisite

| Name                  | Version         |
| --------------------- | --------------- |
| Python                | 3.7             |
| pipenv(Python module) | 2021.5.29 or up |

### Environment setup

0. Initialize environment variable

```
cp env-sample .env
```

1. Initialize Python environment

```
make init
```

2. Enter the environment and start developing

```
pipenv shell
```

3. Start development API service

```
cd api/
uvicorn app:APP
```

The server will run at http://127.0.0.1:8000, and the swagger run at http://127.0.0.1:8000/docs, you can also test all api on swagger

### Formatting

This project uses `black` and `isort` for formatting

```
make format
```

### Linting

This project uses `pylint` and `flake8` for linting

```
make lint
```

### Testing

This project uses `pytest` and its extension(`pytest-cov`) for testing

```
make test
```
