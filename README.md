# WeatherData APIs
As per the Exercise requirement these APIs were develeoped by using wellknown Django Python web framework and database schema designed is SQLite.

Using these apis, we will be able to access weather details for various locaitons and years from 1985-01-01 to 2014-12-31. This data can be filtered by date and location. These APIs also provide statistical information on the weather data.

## Functionalities of the APIs
We can retrieve weather data for a specific date and location
As well as we should be able to retrive statistical information on the weather data, including the maximum, minimum, and total precipitation for a specific date and location

# Installation of the Application
In order to start with setup locally , we suggest create a VirtualEnv locally and then we should use below command to install the required packages for the app.

```
pip install -r requirements.txt
```

# how to initiate the app locally:
Start the server by using the below command (Please make sure you are on the right folder & path where the manage.py script is located )
```
python manage.py runserver
```
Server should be up and running & will be accessible now at our local host i.e http://localhost:8000

# Endpoints:

### Weather data
```
GET /weather/api/
```
This endpoint returns a paginated list of weather records. You can filter the results by date and station using query parameters:
GET /api/weather/?date=19850103&station=USC00257715

### Statistics
```
GET /weather/api/stats/
```
This endpoint returns statistical information about the weather data. You can filter the results by date and station using query parameters, in the same way as the /api/weather/ endpoint.

# Testing
In order to run the tests, we can use pytest module to run unit tests
```
pytest -v ./tests
```

# Deployment / CI CD
We can use Amazon ECS or EKS to deploy the applicaiton. AWS Cloudwatch for logs.

## More information regarding Deployment / CI CD
We can use tools like Docker, Kubernetes to deploy the Services/Backend Services which provide some RESTful apis.
Docker is a tool designed to create, deploy and run applicaitons by using containers. We will use a Dockerfile to create our containers.
Kubernetes is an opensource orchestration system for automating applicaiton deployment, scaling and managment. We will use different kube files, ingress and egress files to deploy applicaitons to different environments like DEV, UAT and PROD.

We can also use tools like AWS CloudFormation, AWS ECS and AWS EKS to deploy applicaiton on cloud.
AWS CloudFormation is good choice for large organization who are having diverse infrastrucure needs. and this AWS CloudFormaiton is not suitable for small organizations.
AWS ECS is suitable for small and startup companies. Its easy to deploy and does not require much operation knowledge to manage deployments and applicaitons on ECS.
AWS EKS is also suitable for large organiations with complex requirements. But its slightly expensive.
