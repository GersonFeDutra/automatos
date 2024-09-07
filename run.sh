#!/bin/bash
chmod +x ./generate.py
chmod +x ./batch.sh
gcc arquivo.c -g
./generate.py > cases.txt
./batch.sh
