#!/bin/bash

DATAPATH=$HOME/datasets/COCO/2014

mkdir -p $DATAPATH
cd $DATAPATH

mkdir -p images annotations

### Images
cd images

echo "Downloading datasets..."
wget http://images.cocodataset.org/zips/train2014.zip
wget http://images.cocodataset.org/zips/val2014.zip
wget http://images.cocodataset.org/zips/test2014.zip

echo Extracting datas...
7z x train2014.zip
7z x val2014.zip
7z x test2014.zip

### Annotations
cd ..

echo "Downloading annotations..."
wget http://images.cocodataset.org/annotations/annotations_trainval2014.zip

echo "Downloading minival annotations..."
wget https://dl.dropboxusercontent.com/s/o43o90bna78omob/instances_minival2014.json.zip?dl=0

echo "Extracting annotations..."
unzip annotations_trainval2014.zip
unzip instances_minival2014.json.zip
mv instances_minival2014.json annotations

echo "Downloading label files..."
wget -c "https://pjreddie.com/media/files/coco/5k.part" --header "Referer: pjreddie.com"
wget -c "https://pjreddie.com/media/files/coco/trainvalno5k.part" --header "Referer: pjreddie.com"
wget -c "https://pjreddie.com/media/files/coco/labels.tgz" --header "Referer: pjreddie.com"

tar xzvf labels.tgz

awk -v abspath=$DATAPATH '{printf("%s%s\n", abspath, $1)}' 5k.part > 5k.txt
awk -v abspath=$DATAPATH '{printf("%s%s\n", abspath, $1)}' trainvalno5k.part > trainvalno5k.txt
