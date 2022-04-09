To run server
`uvicorn main:app`
or 
`gunicorn -w 4 -k uvicorn.workers.UvicornWorker`
