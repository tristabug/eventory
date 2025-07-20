
# Eventory

## Purpose
A lightweight backend API built with Python, Flask, and MongoDB to log and query web events such as page views and clicks. The application is containerized using Docker for easy deployment.

**Design Decisions & Architectural Choices**


## Features
- Create web events via `POST /events`
- Query events via `GET /events`
- Filter by event type and a timerange
- Dockerized setup with MongoDB

## Tech Stack
- Python 3
- Flask
- MongoDB
- Docker & Docker Compose

---

## Getting Started
### Prerequisites
#### Docker
**CLI Command Notes** *- if using Docker Desktop then use ```docker compose``` instead of ```docker-compose``` for all commands.* 

**Option 1**: Install Docker Desktop (one-click-install)
Use this method for an easy one-click-install of both the Docker Engine and Docker Compose, which are both needed to run Eventory. 

    **Docker Desktop Install Docs** (tested Docker Desktop Version: **4.43.2 (199162)**)
        - **Windows**: https://docs.docker.com/desktop/setup/install/windows-install/
        - **MacOS**: https://docs.docker.com/desktop/setup/install/mac-install/
        - **Linux**: https://docs.docker.com/desktop/setup/install/linux/

**Option 2**: Install Docker Engine & Docker Compose
This option includes two separate installs (Docker Engine, Docker Compose). 

    1. **Docker Engine Install Docs** (tested on docker engine version: **28.3.2**)
        - **Ubuntu**: https://docs.docker.com/engine/install/ubuntu/
        - **Centos**: https://docs.docker.com/engine/install/centos/
        - **Debian**: https://docs.docker.com/engine/install/debian/

    2. **Docker Compose Install Docs**(tested on docker compose version: **v2.38.2-desktop.1**)
        - **Docker Compose**: https://docs.docker.com/compose/install/

### Running the App
1. **Clone the Repository**
    ```
    git clone https://github.com/tristabug/eventory.git
    cd eventory
    ```
2. **Start/Launch Docker**

    **Option 1**: start docker *(Docker Engine & Docker Compose installation)*
    - make sure docker is running before using the app using. See the following docs for help.
        - **Docker Engine**: https://docs.docker.com/engine/ 
        - **Docker Compose**: https://docs.docker.com/compose/cli-command/ 

    **Option 2**: launch docker desktop *(Docker Desktop installation)*

3. *(Optional)* Check that docker is running
    - CLI Command: 
        ```
        docker run hello-world
        ```

    - Expected Output:
        ```
        Hello from Docker!
        This message shows that your installation appears to be working correctly.
        ```

4. Check that **port 5001** is free on your machine 
    - **Windows**: powershell or command prompt
        ``` 
        netstat -aon | findstr LISTENING 
        ```
    - **MacOS** terminal
        ```
        lsof -i -n -P | grep LISTEN 
        ```
    - **Linux**: ss
        ``` 
        ss -tuln 
        ```

5. **Docker**: build images & start container
    1. Navigate to the eventory directory
        ``` 
        cd eventory
        ```
    2. Build and start the docker image and container *(if using docker desktop use ```docker compose up --build```)*
        ```
        docker-compose up --build 
        ```
    The API will be exposed at: ``` http://localhost:5000 ```

6. **Docker**: how to stop running the app by stopping docker
    1. Navigate to the eventory directory
        ```
        cd eventory
        ```
    2. Stop the docker container *(if using docker desktop use ```docker compose down```)*
        ```
        docker-compose down 
        ```

---

## API Endpoints
No authentication is required for any endpoint.
- [Show All Events](docs/get.md#show-all-events): GET /events
- [Show Filtered Events](docs/get.md#show-filtered-events): GET /events
- [Show the Count of Events by Type](docs/get.md#show-events-by-the-event-type-and-count): GET /events/stats
- [Create an Event](docs/post.md#create-an-event): POST /events

---

## Consuming the API from Another App
You can interact with this API from any frontend or backend application using HTTP requests.

Example: JavaScript(```fetch```)
    ```javascript
    // Log an event
    fetch('http://localhost:5000/events', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            event_type: 'page_view',
            timestamp: new Date().toISOString()
        })
    });

    // Query events
    fetch('http://localhost:5000/events?type=click')
        .then(res => res.json())
        .then(data => console.log(data));
    ```

---

## Unit Tests
Run the application's unit tests within the docker container. 
1. Navigate to the eventory directory 
    ```
    cd /eventory
    ```
2. Unless already running, build the docker container and images *(if using docker desktop use ```docker compose up --build```)*
    ```
    docker-compose up --build 
    ```
3. Run the unit tests inside the container *(if using docker desktop use ```docker compose run web pytest```)*
    ```
    docker-compose run web pytest
    ```
