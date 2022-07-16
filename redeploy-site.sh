#!/bin/bash
cd project-python-panthers

/usr/bin/git fetch && /usr/bin/git reset origin/main --hard

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build
