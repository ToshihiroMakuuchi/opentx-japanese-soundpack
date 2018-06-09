#!/usr/bin/env python3

# This Python script is used to convert WAV files to a format compatible with
# OpenTX.  A given directory tree is scanned for files ending in .lef32.wav.
# Shell commands are output to convert these files to pcm_s16le using ffmpeg.
# Example usage: ./recode.py en/ > convert.sh

import sys
import os
import shlex

src_dir = sys.argv[1]

print("#!/bin/bash")

for root, _, files in os.walk(src_dir):
    for fname in files:
        if not fname.endswith(".lef32.wav"):
            continue

        fname_ = fname.replace(".lef32.wav", ".wav")
        fpath = os.path.join(root, fname)
        fpath_ = os.path.join(root, fname_)

        print("ffmpeg -i %s -y -acodec pcm_s16le -ar 32000 %s" % (
            shlex.quote(fpath),
            shlex.quote(fpath_)
        ))
        print("rm %s" % shlex.quote(fpath))
