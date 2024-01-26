# POC to trigger multiple concurrent jobs in kubernetes from python
## Steps
1. Install minikube
2. Build the image
```
docker build -t <docker_username>/fake-bg-task
```
where <docker_username> is the username in docker hub
3. Push the image
```
docker push <docker_username>/fake-bg-task
```
where <docker_username> is the username in docker hub
Take into account that you must first be logged in docker hub via `docker login`
4. run
```
make run DOCKER_USERNAME=<your docker hub username>
```
