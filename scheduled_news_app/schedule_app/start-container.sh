#!/bin/bash
echo "[$(date)] Attempting to start git_main_1..." >> /tmp/container_launch.log
/usr/bin/podman --url unix:///run/podman/podman.sock start git_main_1 >> /tmp/container_launch.log 2>&1
