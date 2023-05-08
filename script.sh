#!/bin/bash

for file in *; do
  if [[ -f "$file" ]]; then
    awk 'NR % 2 == 0 { print FILENAME ": " $0 }' "$file"
  fi
done

