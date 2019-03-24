# Garden Optimizer

## Development Setup

* `pipenv install`

* `pipenv shell`

* `export FLASK_APP=services && flask run`

From `client` directory using Node 8.x

* `npm install`

* `npm run serve`

Visit app at http://localhost:8080

## Build

`docker build -t garden-optimizer .`

## Deploy

`docker run -p 80:8080 garden-optimizer`