
# Eventory

## Purpose
A lightweight backend API built with Python, Flask, and MongoDB to log and query web events such as page views and clicks. The application is containerized using Docker for easy deployment.

### Design Decisions & Architectural Choices

---

## Features
- Create web events via `POST /events`
- Query events via `GET /events`
- Filter by event type and a timerange
- Dockerized setup with MongoDB

---

## Tech Stack
- Python 3
- Flask
- MongoDB
- Docker & Docker Compose

---

## Getting Started
### Prerequisites
#### Docker:
** CLI Command Notes: if you decide to install Docker Desktop then use docker compose instead of docker-compose for all commands. 

##### Option 1: Install Docker Desktop (one-click-install)
Use this method for an easy one-click-install of both the Docker Engine and Docker Compose, which are both needed to run Eventory. 
Tested Docker Desktop Version: 4.43.2 (199162)

Installation Docs:
    - How to install docker desktop on Windows: https://docs.docker.com/desktop/setup/install/windows-install/
    - How to install docker desktop on Mac: https://docs.docker.com/desktop/setup/install/mac-install/
    - How to install docker desktop on Linux: https://docs.docker.com/desktop/setup/install/linux/


##### Option 2: Install Docker Engine & Docker Compose
This option includes to separate installs (Docker Engine, Docker Compose). 

    1. Docker Engine (tested on docker engine version: 28.3.2)
        - How to install docker engine on Ubuntu: https://docs.docker.com/engine/install/ubuntu/
        - How to install docker engine on Centos: https://docs.docker.com/engine/install/centos/
        - How to install docker engine on Debian: https://docs.docker.com/engine/install/debian/

    2. Docker Compose (tested on docker compose version: v2.38.2-desktop.1)
        - How to install docker compose: https://docs.docker.com/compose/install/

### Running the App
1. Clone the Repository
    git clone https://github.com/your-username/web-events-api.git
    cd eventory

2. Start/Launch Docker
    a. Run Docker (Docker Engine & Docker Compose installs)
        Make sure docker is running before using the app using the linked docs below.
        - Docker Engine: https://docs.docker.com/engine/ 
        - Docker Compose: https://docs.docker.com/compose/cli-command/ 

    b. Run Docker Desktop (Docker Desktop installs)
        - Launch Docker Desktop 

3. (Optional) Check that Docker is Running - using a CLI
    - CLI Command: docker run hello-world
    - Expected Output:
        Hello from Docker!
        This message shows that your installation appears to be working correctly.

4. Check that port 5001 is free on your machine 
    a. On Windows: powershell or command prompt
            netstat -aon | findstr LISTENING
    b. On Mac: terminal
            lsof -i -n -P | grep LISTEN
    c. On Linux: ss
            ss -tuln

5. Docker: build images & start containers using a CLI
    a. Navigate to the eventory directory
            cd eventory
    b. Build and start the docker image and container
            docker-compose up --build 
        i. Docker Desktop: 
            docker compose up --build
    c. The API will be exposed at: http://localhost:5000 

6. Docker: how to stop running the app (docker) when needed using a CLI
    a. Navigate to the eventory directory
            cd eventory
    b. Stop the docker container (app)
            docker-compose down 
        i. Docker Desktop: 
            docker compose down

## API Endpoints
No authentication is required for any endpoint.
- Show All Events: GET /events
- Show Filtered Events: GET /events
- Show the Count of Events by Type: GET /events/stats
- Create an Event: POST /events

---

## Consuming the API from Another App
    You can interact with this API from any frontend or backend application using HTTP requests.

    Example: JavaScript(Fetch)

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

---

## Unit Tests
Run the application's unit tests within the docker container. 
1. Navigate to the eventory directory: 
        cd /eventory
2. Build the docker container and images (unless already done).
        docker-compose up --build (if using Docker Desktop: docker compose up --build)
3. Run the unit tests inside the container:
        docker compose run web pytest
