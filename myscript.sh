#!/bin/bash

#switch to branch
git checkout "feature/bash"

#create 5 files via loop for-in
for i in {1..5}
do
   touch file$i.txt
done


