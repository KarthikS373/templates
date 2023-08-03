#!/bin/sh

if [ "$1" = "dev" ]; then
    docker-compose --env-file .env.development -f docker-compose.dev.yml up

elif [ "$1" = "dev:build" ]; then
    docker-compose --env-file .env.development -f docker-compose.dev.yml up --build

elif [ "$1" = "prod" ]; then
    docker-compose --env-file .env.production -f docker-compose.yml up 

elif [ "$1" = "prod:build" ]; then
    docker-compose --env-file .env.production -f docker-compose.yml up --build

else
    echo "Please provide a valid arg $1"
fi