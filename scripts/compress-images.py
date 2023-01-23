#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

import subprocess
import os

def compressImageFile(inputFile, outputFile):
    # command = "sips -s format jpeg -s formatOptions normal %s -o %s" % (inputFile, outputFile)
    commands = ['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', 'normal', inputFile, '-o', outputFile]
    # print(command)
    # p = subprocess.Popen(command.split(), stdout = subprocess.DEVNULL)
    p = subprocess.Popen(commands, stdout = subprocess.DEVNULL)
    p.wait()
    return p.returncode == 0 and os.path.exists(outputFile)

def isCompressGood(inputFile, outputFile):
    st0 = os.stat(inputFile)
    st1 = os.stat(outputFile)
    a, b = st0.st_size, st1.st_size
    delta = a - b
    if delta > 5 * 1024:
        print("%s can have better size: %4d -> %4d" % (inputFile, a, b))
        return True
    return False

import shutil
import json

def main():
    from glob import glob
    cacheFile = '.compress-images-cache'
    alreadyChecked = set()
    if os.path.exists(cacheFile):
        with open(cacheFile) as fh:
            alreadyChecked = set(json.load(fh))

    imageFiles = []
    imageFiles += glob("images/*.png") + glob("images/*.jpg")
    # imageFiles += glob("images/media/*/*.png") + glob("images/media/*/*.jpg")
    imageFiles = list(set(imageFiles))
    imageFiles.sort()
    outputDir = "./.compressed-images/"
    shutil.rmtree(outputDir, ignore_errors = True)
    os.makedirs(outputDir) #, exist_ok = True)
    actions = []
    for fi in imageFiles:
        if fi in alreadyChecked: continue
        fo = outputDir + fi.replace("images/", '').replace('/', '_').replace('png', 'jpg')
        # print(fi, fo)
        ok = compressImageFile(fi, fo)
        if not ok: continue
        if isCompressGood(fi, fo):
            actions.append((fo, fi))
            pass
    for fo, fi in actions:
        print('copy %s -> %s' % (fo, fi))
        shutil.copyfile(fo, fi)

    with open(cacheFile, 'w') as fh:
        json.dump(imageFiles, fh)


if __name__ == "__main__":
    main()
