# Docker
- * if using Docker Desktop, then use ```docker compose``` instead of ```docker-compose``` for all commands.* 

#### Versions Used by This App
- **Docker Desktop**: 4.43.2 (199162)
- **Docker Engine**: 28.3.2
- **Docker Compose**: v2.38.2-desktop.1

## Installation
The Docker Engine and Docker Compose are both needed to run this app. To get both installed, you can either install Docker Desktop (1) or install them separately (2).

**Option 1**: Install Docker Desktop (one-click-install)
Use this method for an easy one-click-install of the Docker Engine, Docker Compose, and other Docker components.

- **Docker Desktop Install Docs**
    - **Windows**: https://docs.docker.com/desktop/setup/install/windows-install/
    - **MacOS**: https://docs.docker.com/desktop/setup/install/mac-install/
    - **Linux**: https://docs.docker.com/desktop/setup/install/linux/

**Option 2**: Install Docker Engine & Docker Compose
This option includes two separate installs (Docker Engine, Docker Compose). 

1. **Docker Engine Install Docs**
    - **Ubuntu**: https://docs.docker.com/engine/install/ubuntu/
    - **Centos**: https://docs.docker.com/engine/install/centos/
    - **Debian**: https://docs.docker.com/engine/install/debian/

2. **Docker Compose Install Docs**
    - **Docker Compose**: https://docs.docker.com/compose/install/

## Starting Docker
*per installation method*

- **Option 1**: start docker *(Docker Engine & Docker Compose installation)*
    - make sure docker is running before using the app. See the following docs for help.
        - **Docker Engine**: https://docs.docker.com/engine/ 
        - **Docker Compose**: https://docs.docker.com/compose/cli-command/ 

- **Option 2**: launch docker desktop *(Docker Desktop installation)*

### Check if Docker is Running
CLI Command: 
    ```
    docker run hello-world
    ```

Expected Output:
    ```
    Hello from Docker!
    This message shows that your installation appears to be working correctly.
    ```

## Docker Commands
*all commands need to be made from within the app directory that holds the docker-compose.yml and Dockerfile files.*

- **Build & Start** the docker image and container:
    ```
    docker compose up --build 
    ```
- **Stopping** the docker container (db & app):
    ```
    docker compose down 
    ```

- **Run the unit tests** inside the container:
    ```
    docker compose run web pytest
    ```

- **Find the Flask version** used inside the container:
    ```
    docker exec -it <container_name_or_id> bash
    pip show flask
    ```