# coding:utf-8
import os
import glob
import random

'''
    为数据集生成对应的txt文件
'''
datapath = "/run/media/cug/00077CE80009E4AD/tw/ucm/datas/flow55_2"
train_txt_path = os.path.join(datapath, "train.txt")
train_dir = os.path.join(datapath, "train")

valid_txt_path = os.path.join(datapath, "valid.txt")
valid_dir = os.path.join(datapath, "test")



def gen_txt(txt_path, img_dir):
    f = open(txt_path, 'w')

    image_path_list = glob.glob(os.path.join(train_dir, '*', '*'))
    image_path_list.sort()
    print(len(image_path_list))
    categories = [d.name for d in os.scandir(train_dir) if d.is_dir()]
    print(categories)
    categories.sort()
    print(len(categories))
    class_to_idx = {categories[i]: i for i in range(len(categories))}
    print(class_to_idx)
    idx_to_class = {idx: class_ for class_, idx in class_to_idx.items()}
    print(class_to_idx)


    tmp =[]
    for root, s_dirs, _ in os.walk(img_dir, topdown=True):  # 获取 train文件下各文件夹名称
        for sub_dir in s_dirs:
            i_dir = os.path.join(root, sub_dir)  # 获取各类的文件夹 绝对路径
            img_list = os.listdir(i_dir)  # 获取类别文件夹下所有png图片的路径
            for i in range(len(img_list)):
                # if not img_list[i].endswith('jpg'):  # 若不是png文件，跳过
                #     continue
                label = sub_dir
                num_label = class_to_idx[str(label)]
                img_path = os.path.join(i_dir, img_list[i])
                line = img_path + ',' + str(num_label) + '\n'
                tmp.append(line)

    random.shuffle(tmp)
    for i in tmp:
        f.write(i)
    f.close()


if __name__ == '__main__':
    gen_txt(train_txt_path, train_dir)
    gen_txt(valid_txt_path, valid_dir)