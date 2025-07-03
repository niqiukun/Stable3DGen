#!/usr/bin/env bash

cd /runpod-volume/Stable3DGen || exit 1
git pull
exec /runpod-volume/Stable3DGen/venv/bin/python -u rp_handler.py
