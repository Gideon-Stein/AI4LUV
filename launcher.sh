#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/stein/AI4LLUV
conda activate ai4luv_operational 
python main.py
cd /
