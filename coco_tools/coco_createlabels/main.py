"""
特定クラスの画像ファイルのみを探し, instances_xxx.json から
その画像に対応するラベルファイルを生成する. 
COCO_val2014_000000000123.txt のようなラベルファイルを生成する.
クラス番号は, １クラス分類用の場合, 0になる.
"""

import os
import sys
import shutil
import json
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', default='train')
parser.add_argument('--year', default=2014)
parser.add_argument('--root', default='/home/matsuda/datasets/COCO')
args = parser.parse_args()

YEAR        = args.year
TYPE        = args.type
ROOT        = os.path.join(args.root, str(YEAR))
ANN_FILE    = ROOT + '/annotations/instances_' + TYPE + str(YEAR) + '.json'
CATEGORY_ID = 3

if not TYPE in ['train', 'val']:
    print("\x1b[31mERROR: Argument 'type' (Please choose in ['train', 'val']).\x1b[37m")
    sys.exit(1)

LABEL_DIR   = ROOT + '/labels/' + TYPE + str(YEAR)

# jsonファイルを開き, jsonとして読み込む
json_file = open(ANN_FILE, 'r')
json_dict = json.load(json_file)

name2id_table = {'person'        :0,
                 'bicycle'       :1,
                 'car'           :2,
                 'motorcycle'    :3,
                 'airplane'      :4,
                 'bus'           :5,
                 'train'         :6,
                 'truck'         :7,
                 'boat'          :8,
                 'traffic light' :9,
                 'fire hydrant'  :10,
                 'stop sign'     :11,
                 'parking meter' :12,
                 'bench'         :13,
                 'bird'          :14,
                 'cat'           :15,
                 'dog'           :16,
                 'horse'         :17,
                 'sheep'         :18,
                 'cow'           :19,
                 'elephant'      :20,
                 'bear'          :21,
                 'zebra'         :22,
                 'giraffe'       :23,
                 'backpack'      :24,
                 'umbrella'      :25,
                 'handbag'       :26,
                 'tie'           :27,
                 'suitcase'      :28,
                 'frisbee'       :29,
                 'skis'          :30,
                 'snowboard'     :31,
                 'sports ball'   :32,
                 'kite'          :33,
                 'baseball bat'  :34,
                 'baseball glove':35,
                 'skateboard'    :36,
                 'surfboard'     :37,
                 'tennis racket' :38,
                 'bottle'        :39,
                 'wine glass'    :40,
                 'cup'           :41,
                 'fork'          :42,
                 'knife'         :43,
                 'spoon'         :44,
                 'bowl'          :45,
                 'banana'        :46,
                 'apple'         :47,
                 'sandwich'      :48,
                 'orange'        :49,
                 'broccoli'      :50,
                 'carrot'        :51,
                 'hot dog'       :52,
                 'pizza'         :53,
                 'donut'         :54,
                 'cake'          :55,
                 'chair'         :56,
                 'couch'         :57,
                 'potted plant'  :58,
                 'bed'           :59,
                 'dining table'  :60,
                 'toilet'        :61,
                 'tv'            :62,
                 'laptop'        :63,
                 'mouse'         :64,
                 'remote'        :65,
                 'keyboard'      :66,
                 'cell phone'    :67,
                 'microwave'     :68,
                 'oven'          :69,
                 'toaster'       :70,
                 'sink'          :71,
                 'refrigerator'  :72,
                 'book'          :73,
                 'clock'         :74,
                 'vase'          :75,
                 'scissors'      :76,
                 'teddy bear'    :77,
                 'hair drier'    :78,
                 'toothbrush'    :79
                }
id2name_table = {
                  1:'person',
                  2:'bicycle',
                  3:'car',
                  4:'motorcycle',
                  5:'airplane',
                  6:'bus',
                  7:'train',
                  8:'truck',
                  9:'boat',
                 10:'traffic light',
                 11:'fire hydrant',
                 13:'stop sign',
                 14:'parking meter',
                 15:'bench',
                 16:'bird',
                 17:'cat',
                 18:'dog',
                 19:'horse',
                 20:'sheep',
                 21:'cow',
                 22:'elephant',
                 23:'bear',
                 24:'zebra',
                 25:'giraffe',
                 27:'backpack',
                 28:'umbrella',
                 31:'handbag',
                 32:'tie',
                 33:'suitcase',
                 34:'frisbee',
                 35:'skis',
                 36:'snowboard',
                 37:'sports ball',
                 38:'kite',
                 39:'baseball bat',
                 40:'baseball glove',
                 41:'skateboard',
                 42:'surfboard',
                 43:'tennis racket',
                 44:'bottle',
                 46:'wine glass',
                 47:'cup',
                 48:'fork',
                 49:'knife',
                 50:'spoon',
                 51:'bowl',
                 52:'banana',
                 53:'apple',
                 54:'sandwich',
                 55:'orange',
                 56:'broccoli',
                 57:'carrot',
                 58:'hot dog',
                 59:'pizza',
                 60:'donut',
                 61:'cake',
                 62:'chair',
                 63:'couch',
                 64:'potted plant',
                 65:'bed',
                 67:'dining table',
                 70:'toilet',
                 72:'tv',
                 73:'laptop',
                 74:'mouse',
                 75:'remote',
                 76:'keyboard',
                 77:'cell phone',
                 78:'microwave',
                 79:'oven',
                 80:'toaster',
                 81:'sink',
                 82:'refrigerator',
                 84:'book',
                 85:'clock',
                 86:'vase',
                 87:'scissors',
                 88:'teddy bear',
                 89:'hair drier',
                 90:'toothbrush'
                }

if os.path.isdir(LABEL_DIR):
    shutil.rmtree(LABEL_DIR)

os.makedirs(LABEL_DIR)

print("Creating label text files ...")
for ann in tqdm(json_dict['annotations']):
    cat_id = ann['category_id']
    # ほしいクラスのオブジェクトを含む画像の場合のみ, ラベル情報をファイルに追記
    if cat_id == CATEGORY_ID:
        # image_id から, jsonの imagesリストのインデックスを取得
        image_id = ann['image_id']
        l_image_id = [d.get('id') for d in json_dict['images']]
        index = l_image_id.index(image_id)
        img = json_dict['images'][index]

        file_name = 'COCO_' + TYPE+str(YEAR) + '_' + str(image_id).zfill(12) + '.txt'
        file_path = os.path.join(LABEL_DIR, file_name)
        #print(file_path)
        with open(file_path, 'a') as f:
            x_center = (ann['bbox'][0] + (ann['bbox'][2] / 2)) / img['width']
            y_center = (ann['bbox'][1] + (ann['bbox'][3] / 2)) / img['height']
            width    = ann['bbox'][2] / img['width']
            height   = ann['bbox'][3] / img['height']
            box = "%.6f %.6f %.6f %.6f" % \
                  (x_center, y_center, width, height)
            #name = id2name_table[ann['category_id']]
            #cat_id = name2id_table[name]
            cat_id = 0

            if not os.path.getsize(file_path):
                obj = str(cat_id) + " " + box
            else:
                obj = '\n' + str(cat_id) + " " + box

            f.write(obj)
