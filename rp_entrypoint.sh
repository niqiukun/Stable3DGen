#!/usr/bin/env bash

cd /runpod-volume/Stable3DGen || exit 1
git pull
TORCH_HOME=/runpod-volume/Stable3DGen/.cache/torch exec /runpod-volume/Stable3DGen/venv/bin/python -u rp_handler.py
