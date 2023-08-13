#!/bin/bash

# Run the stress test in scripts
sh ./scripts/pi-cpu-stress.sh

# Once completed, run the python script to parse the data for each log in data/
for file in data/cpu_temp_*.log; do
  python3 main.py "$file"
done