# wally

Diff api results over time.

## Getting Started

Install [docker](https://docs.docker.com/engine/installation/).

    docker-compose up

## Components

The project structure is designed around scalable, containerized microservices.

- core: Python data integration service
- database: [OrientDB](https://github.com/orientechnologies/orientdb) graph data store
- api: [Flask](https://github.com/pallets/flask) RESTful api
- app: [react-redux](https://github.com/reactjs/redux) front-end
- cache: [Redis](https://github.com/antirez/redis) in-memory data store
