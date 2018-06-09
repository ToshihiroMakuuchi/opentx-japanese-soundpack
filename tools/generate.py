#!/usr/bin/env python3

# This Python script parses the CSV index file and generates shell commands to
# invoke the text-to-speech engine.
# Example usage: ./generate.py index.csv > tts.sh

import sys
import csv
import shlex

csv_file = sys.argv[1]
paths = set()
directories = set()

print("#!/bin/bash")

# define text-to-speech function (in this case for macos)
print("""
function tts {
    say -v Samantha --data-format=LEF32@32000 -o $2 $1
}
""")

with open(csv_file, "r") as fh:
    csv_reader = csv.DictReader(fh)
    for row in csv_reader:
        # ignore uncategoriezed entries
        if row["category"] == "":
            continue

        text = row["_text"]
        directory = row["directory"]
        filename = row["filename"]
        filepath = directory + filename + ".lef32.wav"

        # ensure filenames are unique
        assert filepath not in paths
        paths.add(filepath)

        # create directories, if required
        if directory not in directories:
            directories.add(directory)
            print("mkdir -p %s" % shlex.quote(directory))

        # issue tts command
        print("tts %s %s" % (shlex.quote(text), shlex.quote(filepath)))

