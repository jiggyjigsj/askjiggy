#!/bin/bash

if [[ "$1" ]]; then
  echo "Running: $@"
  eval "$@"
else
  source .env
  python3 main.py
fi
