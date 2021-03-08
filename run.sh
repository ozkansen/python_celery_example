#!/usr/bin/env bash

if ! [[ -d .venv ]]; then
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
fi

docker run -d -p 6379:6379 redis:alpine

source .venv/bin/activate
watchmedo auto-restart \
    --directory=./ \
    --pattern=*.py \
    --recursive -- \
    celery -A main \
        worker \
        -B \
        -l DEBUG
