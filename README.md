# Overview

A light-weight and simple python flask API which enables you to provide a link as a url parameter and download videos using youtube-dl. Downloads are all managed server-side, with files being pushed to the user and deleted afterwards (300 seconds).

# Build & Deploy with Docker (inside directory)

```
docker build -t youtube-dl-flask-api:latest . -f dockerfile
docker-compose -p "youtube-dl-flask-api-stack" up -d 
```