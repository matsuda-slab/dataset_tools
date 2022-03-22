import os, sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

NUM_CLASSES = 80

#image_path = '/home/matsuda/datasets/COCO_car/2014/images/train2014/COCO_train2014_000000000149.jpg'
image_path = 'COCO/COCO_train2014_000000002860.jpg'
#image_dir  = os.path.dirname(image_path)
#label_dir  = "labels".join(image_dir.rsplit("images", 1))
#label_path = os.path.join(label_dir, os.path.basename(image_path))
#label_path = os.path.splitext(label_path)[0] + '.txt'
label_path = 'COCO/COCO_train2014_000000002860.txt'

input_image = Image.open(image_path).convert('RGB')
img_w, img_h = input_image.size
print(img_w, img_h)

plt.figure()
fig, ax = plt.subplots(1)
ax.imshow(input_image)

cmap = plt.get_cmap('tab20b')
colors = [cmap(i) for i in np.linspace(0, 1, NUM_CLASSES)]  # cmap をリスト化 (80分割)
bbox_colors = random.sample(colors, NUM_CLASSES)     # カラーをランダムに並び替え (任意)

labels = []
with open(label_path, 'r') as f:
    labels = f.readlines()

for label in labels:
    cls, x, y, w, h = label.split()
    print(x, y, w, h)
    x = float(x) * img_w
    y = float(y) * img_h
    w = float(w) * img_w
    h = float(h) * img_h
    x_min = x - w/2
    y_min = y - h/2
    color = bbox_colors[int(cls)]
    bbox = patches.Rectangle((int(x_min), int(y_min)), int(w), int(h), linewidth=2, edgecolor=color, facecolor='None')
    print(int(x_min), int(y_min), int(w), int(h))
    ax.add_patch(bbox)

plt.axis("off")
plt.savefig("labeled_image.jpg")
