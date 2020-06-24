#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import glob

PATH = os.getcwd()
print(f"Renaming directory in {PATH}")


def find_video_files(directory: str, file_type: str = 'mkv') -> list:
    """Find list of video files in directory"""
    video_files = []
    for file in glob.glob(f"{directory}/*.{file_type}"):
        video_files.append(file)
    return video_files


def main():
    """main"""
    directories = os.listdir()
    print(f"Directories in path: {directories}")

    for dir in directories:
        if os.path.isdir(dir) and not dir.startswith('.') and not dir.endswith('.py'):
            mkv_files = find_video_files(dir, 'mkv')
            print(mkv_files)

            counter = 0 if len(mkv_files) > 1 else ""
            for file in mkv_files:
                print(f"Renaming file in directory: {dir}")
                os.rename(f"{file}", f"{dir}{counter}.mkv")
                counter += 1


if __name__ == '__main__':
    main()