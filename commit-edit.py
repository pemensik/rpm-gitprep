#!/usr/bin/python3
#
# 

import re
import sys
import os

path = None
patch_name = None
patch_number = None

debug = True
dry_run = True

values = [
    ("PATCH_NUMBER",    ["PatchNumber", "PatchNr", "PatchNo"] ),
    ("PATCH_NAME",      ["Patch", "PatchName"] ),
    ("SPEC_CHANGELOG",  ["SpecChangelog", "SpecChlog", "Changelog"] ),
]

if len(sys.argv)>1:
    path = sys.argv[1]
else:
    print("Use parameter with commit message file")
    sys.exit(1)

def parsevalues(message_lines):
    re_keyval = re.compile("(\w+):\s*(.*)\s*")
    values = {}
    for line in message_lines:
        match = re_keyval.match(line)
        if match:
            key = match.group(1)
            v = values.get(key, [])
            v.append(match.group(2))
            values[key] = v
    return values

message_lines = None
new_message = None
values_new = []

with open(path, "r") as f:
    message_lines = f.readlines()

    values_present = parsevalues(message_lines)
    if debug:
        print(values_present)
    for env, names in values:
        value = os.getenv(env)
        if value != None:
            found = None
            for name in names:
                present = values_present.get(name)
                if present != None:
                    found = present
                    break
            if found == None:
                    name = names[0]
                    values_new.append("{0}: {1}\n".format(name, value))

    if debug:
        print("New: ", "\n\t".join(values_new))
    if len(values_present) == 0:
        message_lines.append("\n")
    message_lines.extend(values_new)
    new_message = "".join(message_lines)

if len(values_new)>0:
    if dry_run:
        print(new_message)
    else:
        with open(path, "w") as f:
            f.write(new_message)
else:
    print("No changes")
