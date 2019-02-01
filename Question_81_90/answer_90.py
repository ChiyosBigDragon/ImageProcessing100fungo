import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

## Dicrease color
def dic_color(img):
    img //= 63
    img = img * 64 + 32
    return img

## Database
train = glob("train_*")
train.sort()

db = np.zeros((len(train), 13), dtype=np.int32)
pdb = []

for i, path in enumerate(train):
    img = dic_color(cv2.imread(path))
    ## histogram
    for j in range(4):
        db[i, j] = len(np.where(img[..., 0] == (64 * j + 32))[0])
        db[i, j+4] = len(np.where(img[..., 1] == (64 * j + 32))[0])
        db[i, j+8] = len(np.where(img[..., 2] == (64 * j + 32))[0])

    ## class
    if 'akahara' in path:
        cls = 0
    elif 'madara' in path:
        cls = 1
    db[i, -1] = cls
    pdb.append(path)

# k-Means
Class = 2

feats = db.copy()
np.random.seed(4)
## assign random class 
for i in range(len(feats)):
    if np.random.random() < 0.3:
        feats[i, -1] = 0
    else:
        feats[i, -1] = 1

while True:
    gs = np.zeros((Class, 12), dtype=np.float32)
    change_count = 0

    ## compute gravity
    for i in range(Class):
        gs[i] = np.mean(feats[np.where(feats[..., -1] == i)[0], :12], axis=0)

    ## re-labeling
    for i in range(len(feats)):
        dis = np.square(np.sum(np.abs(gs - feats[i, :12]), axis=1))
        pred = np.argmin(dis, axis=0)
        if int(feats[i, -1]) != pred:
            change_count += 1
            feats[i, -1] = pred

    if change_count < 1:
        break

for i in range(len(train)):
    print(pdb[i], " Pred:", feats[i, -1])
