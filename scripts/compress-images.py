#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

import subprocess
def compressImageFile(inputFile, outputFile):
    command = "sips -s format jpeg -s formatOptions normal %s -o %s" % (inputFile, outputFile)
    # print(command)
    p = subprocess.Popen(command.split(), stdout = subprocess.DEVNULL)
    p.wait()
    return p.returncode == 0 and os.path.exists(outputFile)

import os
def isCompressGood(inputFile, outputFile):
    st0 = os.stat(inputFile)
    st1 = os.stat(outputFile)
    a, b = st0.st_size, st1.st_size
    ratio = (a - b) * 1.0 / a
    if ratio > 0.05:
        print("%s can have better size: %4d -> %4d" % (inputFile, a, b))
        return True
    return False

import shutil
def main():
    from glob import glob
    imageFiles = glob("images/*.png") + glob("images/*.jpg")
    outputDir = "./output-dir/"
    shutil.rmtree(outputDir, ignore_errors = True)
    os.makedirs(outputDir, exist_ok = True)
    actions = []
    for fi in imageFiles:        
        fo = outputDir + fi.replace("images/", '').replace('png', 'jpg')
        ok = compressImageFile(fi, fo)
        if not ok: continue
        if isCompressGood(fi, fo):
            actions.append((fo, fi))
            pass    
    for fo, fi in actions:
        print('copy %s -> %s' % (fo, fi))
        shutil.copyfile(fo, fi)

if __name__ == "__main__":
    main()      
