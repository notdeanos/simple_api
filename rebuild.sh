#!/usr/bin/env sh

CONTAINER=`docker container ls --all | egrep deanmcdonald | awk '{print $1}'`

docker container stop ${CONTAINER}
docker container rm ${CONTAINER}

IMAGE=`docker images --all | egrep deanmcdonald | awk '{print $3}'`

docker image rm ${IMAGE}

docker build -t deanmcdonald/simple-api:0.0.1.RELEASE .
docker container run -d -p 3000:3000 deanmcdonald/simple-api:0.0.1.RELEASE




