- [Flask Api for Deployments](#flask-api-for-deployments)
    - [Getting Started](#getting-started)
        - [Prerequisites](#prerequisites)
        - [Installing](#installing)
    - [Built With](#built-with)
    - [Authors](#authors)
  
# Flask Api for Deployments

A Flask API Rest to save the deployments logs of events, if you want a way to save your deployment log status, you find it !

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The prerequisites you will need to up and running this application

```

Python 3.* (https://www.python.org/downloads/)
Docker (https://www.docker.com/get-started)
MySQL Client (https://dev.mysql.com/doc/mysql-getting-started/en/)
MySQL Databse

```

### Installing

In this example we are going to run this application inside a Docker container, but you can run without container in the same way at your machine

Change configuration File with your Database Credentials

```
mv config.yml.sample config.yml
```

Run the migrate.sh to create the database structure

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
    username: A user to make the requests
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

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/quickstart/) - A Python Microframework

## Authors

* **Lucas Duarte** - *Initial work* - [lusoal](https://github.com/lusoal)

