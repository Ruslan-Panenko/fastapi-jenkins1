# Sharpe explorer backend

## Setup


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
##### For development:

```sh
(venv)$ uvicorn main:app --reload
```

##### For production
```sh
(venv)$ gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

And navigate to `http://127.0.0.1:8000/docs/` to see Swagger documentation.
Or go to `http://127.0.0.1:8000/redoc/` to see ReDoc documentation.

## Tests

To run the tests, `cd` into `tests` directory and run:
```sh
(env)$ pytest
```