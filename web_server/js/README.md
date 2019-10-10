## Create Node.js application

```
node server.js
```

Build docker image by running the following command

```
docker build -t docker.io/sergeyglad/hello-node:v1 .

```

Run container
```
docker run -d -p 8080:8080 docker.io/sergeyglad/hello-node:v1
```

Open web page
```
curl localhost:8080
```
Push your image to registry
```
docker push docker.io/sergeyglad/hello-node:v1
```
