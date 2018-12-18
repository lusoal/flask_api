- [Flask Api for Deployments](#flask-api-for-deployments)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Build with Docker Compose (All the environment)](#build-with-docker-compose-all-the-environment)
    - [Build with Docker only (Application only)](#build-with-docker-only-application-only)
    - [Demonstration](#demonstration)
  - [Built With](#built-with)
  - [Authors](#authors)
  
# Flask Api for Deployments

A Flask API Rest to save the deployments logs of events, if you want a way to save your deployment log status, you find it !

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The prerequisites you will need to up and running this application

```
Docker (https://www.docker.com/get-started)
Docker Compose (https://docs.docker.com/compose/install/)
```

### Build with Docker Compose (All the environment)
---

```
docker-compose up
```
If you want to change de information to access the api just change de environment variables inside the compose.

```
DB_HOST: mysql:3306 (Host of Database)
DB_USER: root (User to access the information)
DB_PASS: admin (Pass to access DB)
DB_SCHEMA: deploy_db (Schema name)
APP_USER: teste (User to get the token from the api)
APP_PASS: 123456 (Password for the user to get the token)
```

Access the application from your Browser to see how it works

```
http://localhost:5000/api/help
```
---
### Build with Docker only (Application only)

In this example we are going to run this application inside a Docker container, but you can run without container in the same way at your machine

Run the migrate.sh to create the database structure on your MySQL DB Instance

```
./migrate.sh
```

Open the config.yml and fill the information

```
database:
  host: the endpoint of your database
  user: user of your database
  pass: pass of your database
  schema: deploy_db (If you had run the ./migrate.sh the patter will be deploy_db)
user:
  username: A user to generate token
  password: password for the user
```

Create the Docker image with the application

```
docker build -t myflaskapp:latest .
```

Run the container exposing the port of the applciation

```
docker run -i -d -p 5000:5000 myflaskapp:latest
```

Access the application from your Browser to see how it works

```
http://localhost:5000/api/help
```


### Demonstration

[![Deploy](http://img.youtube.com/vi/inmcXoVbZYE/0.jpg)](http://www.youtube.com/watch?v=inmcXoVbZYE "Deploy Application")

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/quickstart/) - A Python Microframework

## Authors

* **Lucas Duarte** - *Initial work* - [lusoal](https://github.com/lusoal)

