#!/bin/bash

main_file=day$1.py
test_file=tests/test_day$1.py
input_file=inputs/day$1.txt

if test -f $main_file; then
    echo "$main_file already exists"
else
    cp template.py $main_file
fi

if test -f $test_file; then
    echo "$test_file already exists"
else
    cp tests/test_template.py $test_file
fi

if test -f $input_file; then
    echo "$input_file already exists"
else
    touch $input_file
fi
