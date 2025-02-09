# ProjectTemplate
This is a project template for a python project. It features a logging, data handling, config handling and a template to build and run it in docker. The main idea behind the template is to have a clean working tree.
To enable the setup, adjust the rootFolder in the ./config/rootPath.py file to your root folder name.

## create the docker file
In the Dockerfile, set the workdir to your rootFolder name

`docker build -t <your_app_name> .`
`docker run --env-file=dockerEnvironmentVariables.env <your_app_name>`
