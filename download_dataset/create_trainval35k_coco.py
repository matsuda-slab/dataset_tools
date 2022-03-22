import os
import sys
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--year', default=2014)
args = parser.parse_args()

YEAR = args.year
ROOT = '/home/matsuda/datasets/COCO/' + str(YEAR)
DIRPATH = ROOT + '/annotations'

print("Creating instances_trainval35k.json into " + DIRPATH + " ...")
filepath = os.path.join(DIRPATH, 'instances_train'+str(YEAR)+'.json')
f1 = open(filepath, 'r')
dic1 = json.load(f1)
img1 = dic1['images']
ann1 = dic1['annotations']

filepath = os.path.join(DIRPATH, 'instances_val'+str(YEAR)+'.json')
f2 = open(filepath, 'r')
dic2 = json.load(f2)
img2 = dic2['images']
ann2 = dic2['annotations']

# extend : リストを結合する
img1.extend(img2)
ann1.extend(ann2)

# 共通するキー(info, licenses, categories) はどちらか片方のものをそのまま使う
# images と annotations は, 結合したものをセット
dic2 = {'info':dic1['info'],
      'licenses':dic1['licenses'],
      'categories':dic1['categories'],
      'images':img1,
      'annotations':ann1}

f1.close()
f2.close()

filepath = os.path.join(DIRPATH, 'instances_trainval35k.json')
f2 = open(filepath, 'w')
json.dump(dic2, f2)
