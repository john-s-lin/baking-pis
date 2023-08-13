#!/bin/bash

# Run the stress test in scripts
sh ./scripts/pi-cpu-stress.sh

# Once completed, run the python script to parse the data for each log in data/
directory="data"
file_pattern="cpu_temp_*.log"

for file in $directory/$file_pattern; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        python3 src/main.py "$file"
    fi
done