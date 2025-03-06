# Timeseries application
This is a project for the module "NoSQL Datenbanken (cds-115) FS25".

## Setup
BarTender is intendet to be run in a Docker Container. Therefore, you must have Docker running on your device. 

### Create the docker image
    docker build -t bar_tender .
### Run the container with a mongo-DB
    docker-compose up d

## Test the Application
Go to http://localhost:6969/apidocs/ to access the Swagger docs and tryout the REST interface.

## Dump some example data
This repo has some example data prepared to try out the REST Interface.
### Dump the data
    docker cp ./dump mongodb-container:/data/db/dump