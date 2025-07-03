#!/usr/bin/env bash

cd /runpod-volume/Stable3DGen || exit 1
git pull
source venv/bin/activate
exec python -u rp_handler.py
