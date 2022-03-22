#!/bin/bash

if [ $# == 0 ]; then
  echo "Specify the path which has 'images' and 'labels'."
  exit 1
fi

ROOTPATH=$1

NUM_IMAGES=$(ls -1 $ROOTPATH/images | wc -l)
TRAIN_RATE=0.7
VALID_RATE=0.2
TEST_RATE=0.1
IMG_FORMAT=jpg

NUM_VALID=`echo "$NUM_IMAGES * $VALID_RATE" | bc | awk '{printf("%d", $1)}'`

rm -rf $ROOTPATH/{train,valid,test}
mkdir -p $ROOTPATH/train/{images,labels} \
         $ROOTPATH/valid/{images,labels} \
         $ROOTPATH/test/{images,labels}

if [ "$(ls $ROOTPATH/train/images | wc -l)" -ne $NUM_IMAGES ]; then
  echo "Creating Train Datasets ..."
  cp $ROOTPATH/images/* $ROOTPATH/train/images
  cp $ROOTPATH/labels/* $ROOTPATH/train/labels
fi

### Create Valid Datasets ###
echo "Creating Valid Datasets ..."
for i in `seq $NUM_VALID`
do
  #images=(`ls -d $ROOTPATH/train/images/*`)
  images=(`find $ROOTPATH/train/images -type f`)
  IMG_LEFT=${#images[*]}
  index=$((RANDOM % $IMG_LEFT))
  img=${images[$index]}
  lbl_tmp=`echo $img | sed -E "s/\.$IMG_FORMAT/\.txt/"`
  lbl=`echo $lbl_tmp | sed -E "s/images/labels/"`
  mv $img $ROOTPATH/valid/images
  mv $lbl $ROOTPATH/valid/labels
done

### Create Test Datasets ###
echo "Creating Test Datasets ..."
NUM_TEST=`echo "$NUM_IMAGES * $TEST_RATE" | bc | awk '{printf("%d", $1)}'`
for i in `seq $NUM_TEST`
do
  #images=(`ls -d $ROOTPATH/train/images/*`)
  images=(`find $ROOTPATH/train/images -type f`)
  IMG_LEFT=${#images[*]}
  index=$((RANDOM % $IMG_LEFT))
  img=${images[$index]}
  lbl_tmp=`echo $img | sed -E "s/\.$IMG_FORMAT/\.txt/"`
  lbl=`echo $lbl_tmp | sed -E "s/images/labels/"`
  mv $img $ROOTPATH/test/images
  mv $lbl $ROOTPATH/test/labels
done
