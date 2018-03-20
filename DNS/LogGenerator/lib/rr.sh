#!/bin/bash
index = 1
while IFS='' read -r line || [[ -n "$line" ]]; do
    oldIP=`echo "$line" | awk -F "," {'print $10'}`
    newIP=`sed "${index}q;d" test.txt`
    echo "Replacing $oldIP with '$newIP'"
    newLine=${line/$oldIP/\'$newIP\'}
    echo $newLine >>LOAD_DATA.sql
    index=$(expr $index + 1)
done < "$1"