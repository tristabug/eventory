
# Eventory

**Purpose**
A lightweight backend API built with Python, Flask, and MongoDB to log and query web events such as page views and clicks. The application is containerized using Docker for easy deployment.

### Design Decisions & Architectural Choices
**Python Library for MongoDB**: PyMongo
- Python's recommended way to work with MongoDB. 

**Schema/No Schema**: considering that there's only one resource (events) and neither MongoDB or PyMongo require a schema, I decided to just use query validations for POST requests. 

### Features
- Create web events via `POST /events`
- Query events via `GET /events`
- Filter by event type and a timerange
- Dockerized setup with MongoDB

### Tech Stack
- Python: 3.10
- Flask: 3.1.1
- MongoDB: v5.x
- Docker Engine: 28.3.2
- Docker Compose: v2.38.2-desktop.1
- Docker Desktop: 4.43.2 (199162)

# Setup Instructions
**Prerequisites**
- [Docker Engine & Docker Compose](docs/docker.md#installation)

1. **Clone the Repository**
    ```
    git clone https://github.com/tristabug/eventory.git
    cd eventory
    ```

2. **Start/Launch Docker**
    - If you need help: [Starting Docker](docs/docker.md#starting-docker)
    - Need to [check if Docker is running](docs/docker.md#check-if-docker-is-running)?
    
4. Check that **port 5001** is free on your machine. 
    **Windows**: powershell or command prompt
    ``` 
    netstat -aon | findstr LISTENING 
    ```
    
    **MacOS** terminal
    ```
    lsof -i -n -P | grep LISTEN 
    ```
    
    **Linux**: ss
    ``` 
    ss -tuln 
    ```
    *If port 5001 isn't free, see these [instructions](docs/port.md).*

5. **Docker**: build images & start container
    Navigate to the eventory directory. Then build and start the docker image and container.
        ``` 
        cd eventory
        docker compose up --build
        ``` 

    The API will be exposed at: ``` http://localhost:5000 ```

---

# API Endpoints
No authentication is required for any endpoint.
- [Show All Events](docs/get.md#show-all-events): GET /events
- [Show Filtered Events](docs/get.md#show-filtered-events): GET /events
- [Show the Count of Events by Type](docs/get.md#show-events-by-the-event-type-and-count): GET /events/stats
- [Create an Event](docs/post.md#create-an-event): POST /events

*See [GET examples](docs/get.md) and [POST examples](docs/post.md).*

---

# Unit Tests
Run the application's unit tests within the docker container. 

1. Navigate to the eventory directory. Then build and start the docker image and container.
        ``` 
        cd eventory
        docker compose up --build
        ``` 

3. Run the unit tests inside the container.
    ```
    docker compose run web pytest
    ```

---

# Resources
- [**Docker Commands**](docs/docker.md#docker-commands)