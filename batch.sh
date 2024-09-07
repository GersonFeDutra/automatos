#!/bin/bash

echo "0"
c=0
while read line; do
    out=$(./a.out)
    ret=$?
    if [ $ret -gt 0 ]; then
        echo "$out has taken more than 1sec"
        exit 124
    fi
    if [ $out != "sim" ]; then
        echo "$out failed"
        echo "$out failed"
        echo "$out failed"
        exit 255
    else
        c=$((c+1))
        echo -e '\e[1A\e[K' "$c [$?]"
    fi
done < cases.txt
