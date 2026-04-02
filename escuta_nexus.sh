#!/bin/bash
if [ -z "$1" ]; then
    python3 nexus_spirit.py
else
    python3 nexus_spirit.py "$*"
fi
