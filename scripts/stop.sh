#!/bin/bash
lines=$(docker ps --filter name=octoprint-assistant);
n_lines=$(echo $lines | grep 'octoprint-assistant' | wc -l);
if [[ $n_lines -eq 1 ]]; then
    echo "Stop Container";
    docker stop octoprint-assistant;
fi