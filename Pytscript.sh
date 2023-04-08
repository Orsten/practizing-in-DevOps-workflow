#!/bin/bash

# Switch to needed  branch
git checkout "feature/python"

# create 5 files
for a in {1..5}
 do
  touch file$a.py
done


