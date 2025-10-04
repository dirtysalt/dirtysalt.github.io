#!/usr/bin/env bash
# Copyright (C) dirlt

# find emacs binary.
kernel=`uname -s`
emacs=`which emacs`
if [ $kernel"X" == "DarwinX" ]; then
    emacs="/Applications/Emacs.app/Contents/MacOS/Emacs"
    if [ ! -f $emacs ]; then
        emacs="/Applications/EEEEEmacs.app/Contents/MacOS/Emacs"
    fi
fi

if [ ! -f $emacs ]; then
    echo "cannot find emacs binary!"
    exit 1
fi

# generate html files.
$emacs --batch --script ./scripts/org-export-html.el
if [ $? != 0 ]; then
    echo "emacs org export html failed!"
    exit 1
fi

# post processing html files.
python3 ./scripts/org-post-html.py
