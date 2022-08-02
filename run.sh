#!/bin/bash

echo "open the browser on localhost:8080"

./dump1090 --interactive --net --aggressive | python3 todatabase.py