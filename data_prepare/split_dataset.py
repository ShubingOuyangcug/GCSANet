# coding: utf-8
"""
    将原始数据集进行划分成训练集、验证集和测试集
"""

import os
import glob
import random
import shutil

dataset_dir = os.path.join("/run/media/cug/00077CE80009E4AD/tw/bishe", "shuju23")
train_dir = os.path.join("/run/media/cug/00077CE80009E4AD/tw/bishe/256flow", "23flow73_02", "train")
# valid_dir = os.path.join("..", "..", "Data", "valid")
test_dir = os.path.join("/run/media/cug/00077CE80009E4AD/tw/bishe/256flow", "23flow73_02", "test")

train_per = 0.7
# valid_per = 0.1
test_per = 0.3


def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


if __name__ == '__main__':

    for root, dirs, files in os.walk(dataset_dir):
        for sDir in dirs:
            imgs_list = glob.glob(os.path.join(root, sDir, '*.jpg'))
            # random.seed(666)
            random.shuffle(imgs_list)
            imgs_num = len(imgs_list)

            train_point = int(imgs_num * train_per)
            valid_point = int(imgs_num * (train_per +test_per))

            for i in range(imgs_num):
                if i < train_point:
                    out_dir = os.path.join(train_dir, sDir)
                elif i < valid_point:
                    out_dir = os.path.join(test_dir, sDir)
                # else:
                #     out_dir = os.path.join(test_dir, sDir)

                makedir(out_dir)
                out_path = os.path.join(out_dir, os.path.split(imgs_list[i])[-1])
                shutil.copy(imgs_list[i], out_path)

            print('Class:{}, train:{}, valid:{}'.format(sDir, train_point, valid_point-train_point))