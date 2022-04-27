#!/usr/bin/env python3
import os
import sys
import pathlib

def main(check_run: bool):
    current_path = pathlib.Path().resolve()
    include = ["metslib", "test"]

    additional_options = ""
    if check_run:
        additional_options = " --dry-run --Werror "

    command = f"clang-format {additional_options}-style=file -i "
    for root, dirs, files in os.walk(current_path, topdown=True):
        dirs[:] = [d for d in dirs if d in include]
        command += " ".join(os.path.join(root, f) for f in files if f.endswith(".cc") or f.endswith(".hh"))
        command += " "

    print ("execute " + command)
    result = os.system(command)
    if result != 0:
        print("clang format failure")
        sys.exit(-1)

if __name__ == "__main__":
    args = sys.argv[1:]
    check_run = False
    if len(args) >= 1 and args[0] == "-check":
        check_run = True
    main(check_run)
