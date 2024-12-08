#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/stein/AI4LLUV
sudo conda activate ai4luv_operational 
sudo python main.py
cd /
