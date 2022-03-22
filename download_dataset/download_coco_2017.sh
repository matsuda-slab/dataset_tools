#!/bin/bash

DATAPATH=$HOME/datasets/COCO/2017

CUR=`exec pwd`

mkdir -p $DATAPATH
cd $DATAPATH

mkdir -p images annotations

### Images
cd images

echo "Downloading datasets..."
curl -O http://images.cocodataset.org/zips/train2017.zip
curl -O http://images.cocodataset.org/zips/val2017.zip
curl -O http://images.cocodataset.org/zips/test2017.zip
# curl -O http://images.cocodataset.org/zips/unlabeled2017.zip

echo Extracting datas...
7z x train2017.zip
7z x val2017.zip
7z x test2017.zip
# 7z x unlabeled2017.zip

# rm -f train2017.zip
# rm -f val2017.zip
# rm -f test2017.zip
# rm -f unlabeled2017.zip

### Annotations
cd ..
curl -O http://images.cocodataset.org/annotations/annotations_trainval2017.zip
curl -O http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip
curl -O http://images.cocodataset.org/annotations/image_info_test2017.zip
# curl -O http://images.cocodataset.org/annotations/image_info_unlabeled2017.zip

unzip annotations_trainval2017.zip
unzip stuff_annotations_trainval2017.zip
unzip image_info_test2017.zip
# unzip image_info_unlabeled2017.zip

# rm annotations_trainval2017.zip
# rm stuff_annotations_trainval2017.zip
# rm image_info_test2017.zip
# rm image_info_unlabeled2017.zip

echo "Creating trainval35k dataset..."

cd $CUR
python create_trainval35k_coco.py --year 2017
