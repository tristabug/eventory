# Ports

If port 5001 isn't free, you can update the docker-compose.yml file before runninig the app with a free port on your machine.

Replace ```5001``` under ```ports:``` with a free port on your machine. 

docker-compose.yml:
```yml
    web:
    build: .
    ports:
      - "5001:5000"
    volumes:
      - .:/app
    depends_on:
      - mongo
```