#!/usr/bin/env bash
# Copyright (C) dirlt

echo "********** emacs publish  **********"
# find emacs binary.
kernel=`uname -s`
emacs="emacs"
if [ $kernel"X" == "DarwinX" ]; then
    emacs="/Applications/Emacs.app/Contents/MacOS/Emacs"
fi

# generate html files.
$emacs --batch --script ./scripts/publish.el
if [ $? != 0 ]; then
    echo "emacs publish failed!"
    exit 1
fi

# post processing html files.
echo "********** post publish  **********"
python3 ./scripts/pp-html.py

echo "********** git push master  **********"
git add .
git commit -a -m 'BUILD HTML'
git push origin master
