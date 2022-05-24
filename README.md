# Sharpe explorer backend

## Requirements

The development was on ubuntu 20.04+ machines.

Version of python is 3.8

## Initial Setup

Go to src/app/core/ and copy secrets.json.example into secrets.json and change your secrets.

## Development Setup

Create a virtual environment to install dependencies in and activate it:

```sh
$ cd sharpe_explorer_backend/src/app
$ python3 -m venv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies, you can run server.

```sh
(venv)$ uvicorn main:app --reload
```

And navigate to `http://127.0.0.1:8000/docs/` to see Swagger documentation.
Or go to `http://127.0.0.1:8000/redoc/` to see ReDoc documentation.

## Production Setup

To run this Docker container you need docker and docker-compose
```sh
$ docker-compose up -d
```
Or you could run it with docker only.

## Tests

To run the tests, `cd` into `tests` directory and run:
```sh
(env)$ pytest
```