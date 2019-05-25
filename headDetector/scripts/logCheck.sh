#!/bin/bash

# This generates a file every 5 minutes

while true; do

	grep "avg" ../train.log
	sleep 1
	clear

done
