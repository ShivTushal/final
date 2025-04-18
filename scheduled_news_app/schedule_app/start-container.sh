#!/bin/bash
echo "[$(date)] Attempting to start git_main_1..." >> /tmp/container_launch.log
podman start git_main_1 >> /tmp/container_launch.log 2>&1
