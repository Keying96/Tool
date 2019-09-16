# -*- coding:utf-8 -*-
#图片按顺序加载
#第1~3次第1层和第9层都在,第3次8张
#第4~6次第2层和第8层都在,第6次4张
#第7~11次第3层和第7层都在,第11次8张
#第12~22次第4层和第6层都在,第22次4张
#第23~43次只有第5层
#第1层,第9层: 2*12 + 8 = 32
#第2层,第8层: 5*12 + 4 = 64
#第3层,第7层: 10*12 + 8 = 128
#第4层,第6层: 21*12 + 4 = 256
#第5层: 42*12 + 8 = 512
#共1472张图片

#最后得到的文件名形式"00000(图片名)_1(图片所在层数)_1(图片在所在层数的位置)"
import os
import numpy as np
import filetype

#重命名的同时添加文件名
def rename_images(images_file_root, dirs_root_name):
    """
    :param images_file_root:图片所在的文件夹的路径地址
    " /media/chloe/Zhu08032964448/Study/LearningToSeeInTheDark/result/visualizeImages/00000/"

    :param dirs_root_name: 图片名字
    dirs_root_name: 00001

    :return:
    """
    file_list = os.listdir(images_file_root)
    # print  file_list

    total_num = len(file_list)
    # print (file_list[3](-3:))
    i = 0
    for item in file_list:
        item_root = os.path.join(images_file_root, item)
        if os.path.isfile(item_root):
            # print ("item_root: " + item_root)
            kind = filetype.guess(item_root)
            if kind.extension == 'png':
                item = int(item[16:-1])
                file_list[i] = item
                i = i + 1


    file_list.sort()
    print file_list

    layer_flag = 1
    j = 0
    j_end_lists = [0, 32, 64, 128, 256, 512, 256, 128, 64, 33]

    for item in file_list:
        # if item.endswith('.png'):
        item_name = "individualImage(" + str(item) + ")"
        item_root = os.path.join(images_file_root, item_name)
        if os.path.isfile(item_root):
            # print ("item_root: " + item_root)
            kind = filetype.guess(item_root)
            if kind.extension == 'png':

                new_name = str(dirs_root_name) + '_' + format(str(layer_flag)) + '_' + format(str(j)) + '.png'
                print ("new_name; " +  new_name)
                src = os.path.join(images_file_root,item_name)
                dst = os.path.join(images_file_root,new_name)
                os.rename(src, dst)
                j = j + 1

                while (j >= j_end_lists[layer_flag]):
                    j = 0
                    layer_flag = layer_flag + 1


def get_dirs_name(input_root):
    '''get dir names by input root

    :param input_root:
    :return:
    '''

    if os.path.isdir(input_root):
        for root, dirs, files in os.walk(input_root):
            for dirs_root_name in dirs:
                curr_root = os.path.join(input_root, dirs_root_name)
                if os.path.isdir(curr_root):
                    # print ("curr_root: " + curr_root)
                    # print ("dis_name: " + dirs_root_name)
                    rename_images(curr_root, dirs_root_name)
                    # for root, dirs, files in os.walk(curr_root):
                    #     for dirs_name in dirs:
                    #         curr_dir = os.path.join(curr_root, dirs_name)
                    #         print ("curr_root: " + curr_root)
                    #         print ("dis_name: " + dirs_name)
                            # rename_images(curr_dir, dirs_name, dirs_root_name)
                            # rename_images(curr_dir, dirs_name)
                            # print("curr_dir: " + str(curr_dir))
                            # print("dirs_name: " + str(dirs_name))
                            # print("dirs_root_name: " + dirs_root_name)

def main():
    input_root = '/media/chloe/Zhu08032964448/Study/LearningToSeeInTheDark/result/visualizeImages/'
    get_dirs_name(input_root)

if __name__ == '__main__':
    main()