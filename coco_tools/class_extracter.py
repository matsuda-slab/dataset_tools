"""
COCOデータセットから特定クラスの画像のみ抽出し,
trainval35k.txt のような テキストファイルを生成する
"""

import os
import sys
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--type', default='trainval')
parser.add_argument('--year', default=2014)
parser.add_argument('--root', default='/home/matsuda/datasets/COCO_car')

args = parser.parse_args()

YEAR        = args.year
TYPE        = args.type
ROOT        = os.path.join(args.root, str(YEAR))
ANN_FILE    = None
output_file = None
CATEGORY_ID = 3     # category 'car' id


if args.type in ['trainval']:
    ANN_FILE = ROOT + '/annotations/instances_trainval35k.json'
    output_file = os.path.join(ROOT, 'trainvalno5k.txt')
elif args.type in ['train', 'val']:
    ANN_FILE = ROOT + '/annotations/instances_' + TYPE + str(YEAR) + '.json'
    output_file = os.path.join(ROOT, TYPE + 'no5k.txt')
elif args.type in ['minival']:
    ANN_FILE = ROOT + '/annotations/instances_minival' + str(YEAR) + '.json'
    output_file = os.path.join(ROOT, '5k.txt')
else:
    print("\x1b[31mArgument error: --type (please choose in ['train', 'val', 'trainval', 'minival'])\x1b[37m")
    sys.exit(1)

f = open(ANN_FILE, 'r')
dic = json.load(f)

path_list = []

if args.type == 'trainval':
    for ann in tqdm(dic['annotations']):
        cat_id = ann['category_id']
        if cat_id == CATEGORY_ID:
            # image_id から, jsonの imagesリストのインデックスを取得
            image_id = ann['image_id']
            l_image_id = [d.get('id') for d in dic['images']]
            index = l_image_id.index(image_id)
            img = dic['images'][index]

            image_path = None
            if 'val' in img['coco_url']:
                image_name = "COCO_val" + str(YEAR) + '_' + str(image_id).zfill(12) + ".jpg"
                image_path = os.path.join(ROOT, "images", 'val'+str(YEAR), image_name)
            else:
                image_name = "COCO_train" + str(YEAR) + '_' + str(image_id).zfill(12) + ".jpg"
                image_path = os.path.join(ROOT, "images", 'train'+str(YEAR), image_name)
    
            if not image_path in path_list:
                path_list.append(image_path)

elif args.type == 'minival':
    for ann in tqdm(dic['annotations']):
        cat_id = ann['category_id']
        if cat_id == CATEGORY_ID:
            image_id = ann['image_id']
            image_name = "COCO_val" + str(YEAR) + '_' + str(image_id).zfill(12) + ".jpg"
            image_path = os.path.join(ROOT, "images", 'val'+str(YEAR), image_name)

            if not image_path in path_list:
                path_list.append(image_path)

else:
    for ann in tqdm(dic['annotations']):
        cat_id = ann['category_id']
        if cat_id == CATEGORY_ID:
            image_id = ann['image_id']
            image_name = "COCO_" + TYPE + str(YEAR) + '_' + str(image_id).zfill(12) + ".jpg"
            image_path = os.path.join(ROOT, "images", TYPE+str(YEAR), image_name)
    
            if not image_path in path_list:
                path_list.append(image_path)

with open(output_file, 'w') as outfile:
    for i in path_list:
        outfile.write(i + '\n')
