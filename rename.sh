#!/bin/sh

SOURCE="$1"
FILE_TYPE="$2"
TARGET=${3:-$SOURCE}

function print_usage() {
    cat << EOF
Usage: ./rename.sh [--help|source] [file_type] [target]
     --help                     Displays help file
     source                     Source of rename folder
     file_type                  File extension type      
     target                     Target of new file folder
EOF
}

function files_in_directory(){
  files=$(find $SOURCE/* -maxdepth 1 -type d)
  echo "Directories found in path: $files"
}

function search_file_in_directory(){
  target_files=()
  for entry in "${files}/*.${FILE_TYPE}"; do
    target_files+=($entry)
  echo "$FILE_TYPE files found in directory: $target_files"
  done
}

function rename_files(){
  counter=0
  for file in ${target_files[@]}; do
    new_name=`basename $(dirname "$file")`
    echo $file
    echo $new_name
    if [ ${#target_files[@]} == 1 ]; then
      mv $file "$TARGET/$new_name.$FILE_TYPE"
    else
      mv $file "$TARGET/$new_name-$counter.$FILE_TYPE"
      counter+=1
    fi
  done
}

function main(){
    files_in_directory
    if [ -z "$files" ]; then
      echo "No directory found"
    else
      search_file_in_directory
    fi
    if [ ${#target_files[@]} -ne 0 ]; then
      rename_files
      exit 0
    fi
    exit 1
}

main