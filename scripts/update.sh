#!/bin/bash
lines=$(docker ps --filter name=octoprint-assistant);
n_lines=$(echo $lines | wc -l);
if [[ $n_lines -eq 2 ]]; then
    echo "Stop Container";
    docker stop octoprint-assistant;
fi

lines=$(docker ps -a --filter name=octoprint-assistant);
n_lines=$(echo $lines | wc -l);
if [[ $n_lines -eq 2 ]]; then
    echo "Remove Container";
    docker rm octoprint-assistant;
fi
docker pull huakunshen/octoprint-assistant;
docker run --rm -d -p 7000:8000 \
    --name octoprint-assistant \
    --env-file .env \
    huakunshen/octoprint-assistant;