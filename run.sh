#!/bin/bash
chmod +x ./generate.py
chmod +x ./degenerate.py
chmod +x ./batch.sh
chmod +x ./debatch.sh
#gcc arquivo.c -g
gcc -g -O3 -Wall -pedantic arquivo.c
./generate.py > cases.txt
./degenerate.py > no-cases.txt
./batch.sh
./debatch.sh
