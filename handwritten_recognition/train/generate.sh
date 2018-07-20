#!/bin/bash
# 作者：李可艺
# 创建于：2018-7-18

touch train.txt
touch val.txt

ls -all ./image | shuf >> train.txt
tail -300 >> val.txt
