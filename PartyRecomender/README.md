# PartyRecommender

Create a collaborative Spotify playlist for your friends/colleagues which will fit for each person with a power of 
recommendation systems

## Run the service
Change the docker-compose file to 
```yaml
version: "3"
services:
  auth_server:
    build: auth_server/
    container_name: auth_server
    ports:
      - "5000:5000"
  rec_sys:
    build: recommender/
    container_name: rec_sys
    ports:
      - "8000:8000"
volumes:
  dbdata:
    driver: local
```
then 
```
docker-compose up --build
```