#!/usr/bin/env sh

S_FLAG=false

while getopts ":s" opt; do
  case $opt in
    s)
      S_FLAG=true
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

CONTAINER=`docker container ls --all | egrep deanmcdonald | awk '{print $1}'`

docker container stop ${CONTAINER}
docker container rm ${CONTAINER}

IMAGE=`docker images --all | egrep deanmcdonald | awk '{print $3}'`

docker image rm ${IMAGE}

docker build -t deanmcdonald/simple-api:0.0.1.RELEASE .
docker container run -d -p 3002:3002 deanmcdonald/simple-api:0.0.1.RELEASE

if $S_FLAG; then
  echo "Pushing to pihole2"
  rsync -aqz . dean@192.168.0.6:simple_api/
  ssh pihole2 "docker build -t deanmcdonald/simple-api:0.0.1.RELEASE simple_api/"
  ssh pihole2 "docker container run -d -p 3002:3002 deanmcdonald/simple-api:0.0.1.RELEASE"
fi



