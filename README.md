# ProjectTemplate
This is a project template for a python project

## create the docker file
In the file rootPath, adjust the rootFolder to the rootFolder of this git repo
In the Dockerfile, set the workdir to your rootFolder name

docker build -t <your_app_name> .
docker run --env-file=dockerEnvironmentVariables.env <your_app_name>