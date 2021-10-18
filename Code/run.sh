#!/bin/bash

date > log.txt # start time
python3 start.py >> log.txt
date >> log.txt # end time
mv log.txt ../Results/ # store the log
