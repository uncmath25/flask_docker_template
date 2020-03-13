# Dockerized Flask Template

### Description:
This project shows how to Dockerize a Flask web server.  A core Docker image is built using Flask and can be easily developed locally.  This dev image is wrapped by a nginx / uwsgi prod image,  which imports from the dev image and is agnostic to the core image's logic, allowing for reusue of this prod image over any dev image.

### Local Usage:
1. Run ` make ` to build, flake and test the dev Flask web server Docker image
1. Run the dev container locally with ` make start `
1. Stop the container with ` make stop `
1. **test.sh** provides a testing script stub to write sample curl requests to the Flaks web server (e.g. POST requests)

(Note: for use with AWS creds, a **.env.dev** is expected based upon the template given by ".env.dev.sample": please provide this file)

### Deployment:
` make deploy ` offers a deployment stub demonstrating how the prod Docker image could be deployed to AWS ECR, for use with ECS (ideally as part of a CI/CD pipeline)
