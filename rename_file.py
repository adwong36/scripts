#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides the user a tool to rename files with specified file type in a directory to replace with the parent
folder name.

For usage details, use the following command
python rename_file.py -h
"""
import argparse
import glob
import os

PATH = os.getcwd()
print(f"Renaming directory in {PATH}")
PARSER = argparse.ArgumentParser(description='Process user input')


def parse_arguments():
    """Parsing arguments from input"""
    PARSER.add_argument('source', nargs='?', default=PATH, type=str, help='source path to rename file')
    PARSER.add_argument('-t', default='mkv', dest='file_type', type=str,
                        help='Specify file extension type, default: mkv')
    return PARSER.parse_args()


def search_file_type(directory: str, file_type: str = 'mkv') -> list:
    """Find list of video files in directory"""
    found = []
    for file in glob.glob(f"{directory}/*.{file_type}"):
        found.append(file)
    print(f"File found: {found}")
    return found


def main():
    """main"""
    arg = parse_arguments()
    directories = os.listdir(os.path.join(arg.source))
    print(f"Directories in path: {directories}")

    for dir in directories:
        if os.path.isdir(dir) and not dir.startswith('.') and not dir.endswith('.py'):
            file_found = search_file_type(dir, arg.file_type)

            counter = 0 if len(file_found) > 1 else ""
            for file in file_found:
                print(f"Renaming {arg.file_type} file in directory: {dir}")
                os.rename(f"{file}", f"{dir}{counter}.{arg.file_type}")
                if isinstance(counter, int):
                    counter += 1


if __name__ == '__main__':
    main()
