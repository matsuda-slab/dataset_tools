"""
データセットのtrain, valid, test のディレクトリを元に,
画像へのフルパスを記述したリスト (train.txt, valid.txt, test.txt) を生成する
"""

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('root', help='train, valid, test があるパス')

args = parser.parse_args()

ROOT = args.root

output_file_train = os.path.join(ROOT, 'train.txt')
output_file_valid = os.path.join(ROOT, 'valid.txt')
output_file_test  = os.path.join(ROOT, 'test.txt')

train_dir = os.path.join(ROOT, 'train/images')
valid_dir = os.path.join(ROOT, 'valid/images')
test_dir  = os.path.join(ROOT, 'test/images')

path_list_train = os.listdir(train_dir)
path_list_valid = os.listdir(valid_dir)
path_list_test  = os.listdir(test_dir)

with open(output_file_train, 'w') as outfile:
    for i in path_list_train:
        path = os.path.join(train_dir, i)
        outfile.write(path + '\n')

with open(output_file_valid, 'w') as outfile:
    for i in path_list_valid:
        path = os.path.join(valid_dir, i)
        outfile.write(path + '\n')

with open(output_file_test, 'w') as outfile:
    for i in path_list_test:
        path = os.path.join(test_dir, i)
        outfile.write(path + '\n')
