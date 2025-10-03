#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import glob
import os
import sys


def process_directory(dir):
    os.chdir(dir)

    org_files = glob.glob("src/*.org")
    used_images = []
    for f in org_files:
        res = parse_used_images(f)
        used_images.extend(res)

    extensions = ['jpg', 'jpeg', 'png', 'svg', 'gif', 'pdf', 'html', 'webp']
    repo_images = []
    for ext in extensions:
        repo_images.extend(glob.glob('images/*.' + ext))
        repo_images.extend(glob.glob('images/media/*/*.' + ext))
    repo_images = [x[len("images/"):] for x in repo_images]

    used_images_set = set((x[0] for x in used_images))
    repo_images_set = set(repo_images)

    fail = False
    for f, src in used_images:
        if f not in repo_images_set:
            print('Image ref missing: %s  ==>  %s' % (f, src))
            fail = True

    for f in repo_images:
        if f not in used_images_set:
            print("Image ref unused: %s" % f)
            # fail = True

    return fail


def parse_used_images(file):
    ref_pfx = "[[../images/"
    bad_pfx_list = ["[[file:images/", "[[file:../images/", "[[images/"]
    used_images = []

    with open(file) as fh:
        for s in fh:
            if any((s.find(x) != -1 for x in bad_pfx_list)):
                print("Invalid image ref: %s ==> %s" % (file, s))
                continue

            if s.find(ref_pfx) == -1:
                continue

            ss = s.split()
            for s in ss:
                if not s.startswith(ref_pfx):
                    continue
                p = s.find(']')
                path = s[len(ref_pfx):p]
                used_images.append((path, file))
    return used_images


def main():
    DIR = '/Users/dirlt/repo/dirtysalt.github.io/'
    import sys
    dir = sys.argv[1] if len(sys.argv) > 1 else DIR
    fail = process_directory(dir)
    if fail:
        sys.exit(1)


if __name__ == '__main__':
    main()
