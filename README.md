# Timeseries application
This is a project for the module "NoSQL Datenbanken (cds-115) FS25".

## Environment Variables
The template has a file for loading environment variables into the docker container. It is recommended to run the command, to prevent pushing the variables to the git repo.
### Ignore Environment Variables Change
        git update-index --assume-unchanged dockerEnvironmentVariables.env

## Create the docker file
In the Dockerfile, set the workdir to your rootFolder name

### Create the docker image
    docker build -t bar_tender .
### Run the container with the environments variables
    docker run -d --env-file=dockerEnvironmentVariables.env -p 6969:6969 bar_tender
