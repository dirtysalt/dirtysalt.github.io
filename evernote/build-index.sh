#!/usr/bin/env bash
# Copyright (C) dirlt

ROOT=`dirname "$0"`
cd $ROOT

dirs=""
for d in `find . -maxdepth 1 -type d`
do
    if [ $d != "." ]; then
        dirs="$dirs $d"
    fi
done

python3 build-index.py $(echo $dirs)
