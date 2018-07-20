#!/bin/bash
# 作者：李可艺
# 创建于：2018-7-18

EXAMPLE=trains/imagenet
DATA=trains/imagenet 
TOOLS=build/tools
 
$TOOLS/compute_image_mean $EXAMPLE/mydata_train_lmdb \ 
  $DATA/mydata_mean.binaryproto
