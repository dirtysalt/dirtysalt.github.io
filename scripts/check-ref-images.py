#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import glob
import os
import sys

# import pathlib
# home_path = str(pathlib.Path.home()) + '/repo/dirtysalt.github.io/'
home_path = os.environ['HOME'] + '/repo/dirtysalt.github.io/'
print(home_path)
image_path = home_path + 'images/'
src_path = home_path + 'src/'

ref_images = []
repo_images = []


def check_images_path(file):
    ref_pfx = "[[../images/"
    bad_pfx_list = ["[[file:images/", "[[file:../images/", "[[imaes/"]

    with open(file) as fh:
        for line in fh:
            if any((line.find(x) != -1 for x in bad_pfx_list)):
                print("bad reference in '%s': '%s'" % (file, line))
                continue

            if line.find(ref_pfx) == -1:
                continue
            ss = line.split()
            for s in ss:
                path = None
                if s.startswith(ref_pfx):
                    p = s.find(']')
                    path = s[len(ref_pfx):p]
                if path:
                    ref_images.append((path, file))


def main():
    fs = glob.glob(src_path + "*.org")
    for f in fs:
        check_images_path(f)

    extensions = ['jpg', 'png', 'svg', 'gif', 'pdf', 'html', 'webp']
    fs = []
    for ext in extensions:
        fs.extend(glob.glob(image_path + '*.' + ext))
        fs.extend(glob.glob(image_path + 'media/*/*.' + ext))

    for f in fs:
        repo_images.append(f[len(image_path):])

    ref_images_set = set((x[0] for x in ref_images))

    fail = False
    for f, src in ref_images:
        if f not in repo_images:
            print('ref missing = %s  ==>  %s' % (f, src))
            if not f.endswith('.gif'):
                fail = True

    for f in repo_images:
        if f not in ref_images_set:
            print("ref unused = %s" % f)
            # fail = True

    if fail:
        sys.exit(1)


if __name__ == '__main__':
    main()
