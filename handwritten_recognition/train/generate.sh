#!/bin/bash

touch train.txt
touch val.txt

ls -all ./image | shuf >> train.txt
tail -300 >> val.txt
