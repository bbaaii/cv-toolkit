#!/bin/bash
EXAMPLE=trains/imagenet
DATA=trains/imagenet 
TOOLS=build/tools
 
$TOOLS/compute_image_mean $EXAMPLE/mydata_train_lmdb \ 
  $DATA/mydata_mean.binaryproto