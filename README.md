# faas

Spring-boot webapplication

## Prerequisites for building and deploying your application locally.

To build spring application need jdk and jre and application related dependencies

## Run

To run build artifact use command 
 
 ```bash
java --jar webapp.war
```
## Build and Deploy instructions for web application on AWS EC2 instance .
create code deployment agent for the instance on which deployment is to performed.

create code deployment group attached to the code deployment agent.

setup a circle ci project to trigger the the web application .

set up circle ci config file to send the web app to code deployment agent in aws .

code deployment agent will deploy the web app to the instance.

step-1:- bulid the AMI for the instance using curl command
```bash
curl -u account number of circleci \-d build_parameters[CIRCLE_JOB]=build \link of the git AMI repository 
```

step-2: Build the infrastructure i.e terraform 
```bash
terraform apply
```

step-3:- after applying terraform deploy the web app code to circle ci using curl command
```bash
curl -u account number of circleci \-d build_parameters[CIRCLE_JOB]=build \link of the git Web-app repository
```

step-4:- Build lambda function as a service using curl command
```bash
curl -u account number of circleci \-d build_parameters[CIRCLE_JOB]=build \link of the git fass repository
``` 