#!/bin/bash
bash ./stop.sh

cp ./config/default ./config/default.bk

lines=$(docker ps -a --filter name=octoprint-assistant);
n_lines=$(echo $lines | grep 'octoprint-assistant' | wc -l);
if [[ $n_lines -eq 1 ]]; then
    echo "Remove Container";
    docker rm octoprint-assistant;
fi
docker pull huakunshen/octoprint-assistant;
docker run --rm -d -p 7000:8000 \
    --name octoprint-assistant \
    --env-file .env \
    huakunshen/octoprint-assistant;

cp ./config/default.bk ./config/default
rm ./config/default.bk