# -*- coding:utf-8 -*-
'''Rename images name
在使用这个工具前需要把individualImage.png 重命名为 individualImage (0).png
By the name of Images's file, to rename the images name.
'''
import os
import numpy as np

#第1~3次第1层和第9层都在
def rename_images(images_file_root, dirs_name):
    file_list = os.listdir(images_file_root)
    # print  file_list

    total_num = len(file_list)
    file_list.sort(key = len)
    # print file_list

    i = 0
    j = 0
    for item in file_list:
        # if item.endswith('.png'):
        new_name = str(dirs_name)+'_' + format(str(i)) + '_' + format(str(j)) + '.png'
        src = os.path.join(images_file_root,item)
        dst = os.path.join(images_file_root,new_name)
        os.rename(src, dst)
        j = j + 1
        # print ("i = " + str(i))
        # print ("j = " + str(j))

        while (j == 12):
            i = i + 1
            j = 0#     img = images[i]
    #     print ("i: " + str(i))
    #
    #     ax.imshow(img)
    #
    #     # Remove ticks.
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #
    # # Ensure the plot is shown correctly with multiple plots
    # # in a single Notebook cell.
    # title = dirs_root_name
    # plt.show()

#重命名的同时添加文件名
def rename_images(images_file_root, dirs_name, dirs_root_name):
    """
    :param images_file_root:图片所在的文件夹的路径地址
    " /media/chloe/Zhu08032964448/Study/LearningToSeeInTheDark/result/visualizeImages/00000/1"

    :param dirs_name:图片所在文件夹的文件名(代表本图片是在第几次被保存)
    dirs_name: 1

    :param dirs_root_name: 图片名字
    dirs_root_name: 00001

    :return:
    """
    file_list = os.listdir(images_file_root)
    # print  file_list

    total_num = len(file_list)
    file_list.sort(key = len)
    # print file_list

    i = 0
    j = 0
    for item in file_list:
        # if item.endswith('.png'):
        new_name = str(dirs_root_name)+ '_' + str(dirs_name) +'_' + format(str(i)) + '_' + format(str(j)) + '.png'
        src = os.path.join(images_file_root,item)
        dst = os.path.join(images_file_root,new_name)
        os.rename(src, dst)
        j = j + 1
        # print ("i = " + str(i))
        # print ("j = " + str(j))

        while (j == 12):
            i = i + 1
            j = 0

def rename(images_file_root, dirs_name, dirs_root_name, i_start, j_end):
    """
    :param images_file_root:图片所在的文件夹的路径地址
    " /media/chloe/Zhu08032964448/Study/LearningToSeeInTheDark/result/visualizeImages/00000/1"

    :param dirs_name:图片所在文件夹的文件名(代表本图片是在第几次被保存)
    dirs_name: 1

    :param dirs_root_name: 图片名字
    dirs_root_name: 00001

    :param i_start: 本次保存从第几层开始

    :return:
    """
    file_list = os.listdir(images_file_root)
    # print  file_list

    total_num = len(file_list)
    file_list.sort(key=len)
    # print file_list

    flag_start = 0
    i = i_start
    j = 0
    for item in file_list:
        # if item.endswith('.png'):
        new_name = str(dirs_root_name) + '_' + str(dirs_name) + '_' + format(str(i)) + '_' + format(str(j)) + '.png'
        src = os.path.join(images_file_root, item)
        dst = os.path.join(images_file_root, new_name)
        os.rename(src, dst)
        j = j + 1
        # print ("i = " + str(i))
        # print ("j = " + str(j))

        if flag_start == 0:
            if j == j_end:
                flag_start = flag_start +1
                i = i + 1
                j = 0
        else:
            while (j == 12):
                i = i + 1
                j = 0


#第1~3次第1层和第9层都在,第3次8张
#第4~6次第2层和第8层都在,第6次4张
#第7~11次第3层和第7层都在,第11次8张
#第12~22次第4层和第6层都在,第22次4张
#第23~43次只有第5层
# class RenameImagesFactory():
#     """
#     根据图片所在的文件夹名字dirs_name,修改i的起始值
#     """
def rename_images(curr_dir, dirs_name, dirs_root_name):
    """
    根据图片所在的文件夹名字dirs_name,修改i的起始值
    :param self:
    :param curr_dir:
    :param dirs_name:
    :param dirs_root_name:
    :return:
    """
    print ("curr_dir: " + curr_dir)
    print ("dirs_name: " + dirs_name)
    print ("dirs_root_name: " + dirs_root_name)

    dirs_name = int(dirs_name)
    j_end = 12

    if 1<= dirs_name <=3:
        if dirs_name == 3:
            j_end = 7
        i_start = 0
        print("now from: " + str(i_start))
        rename(curr_dir, dirs_name, dirs_root_name, i_start, j_end)
    elif 4 <= dirs_name <= 6:
        if dirs_name == 6:
            j_end = 3
        i_start = 1
        print("now from: " + str(i_start))
        rename(curr_dir, dirs_name, dirs_root_name, i_start, j_end)
    elif 7 <= dirs_name <= 11:
        if dirs_name == 11:
            j_end = 7
        i_start = 2
        print("now from: " + str(i_start))
        rename(curr_dir, dirs_name, dirs_root_name, i_start, j_end)
    elif 12 <= dirs_name <= 22:
        if dirs_name == 22:
            j_end = 3
        i_start = 3
        print("now from: " + str(i_start))
        rename(curr_dir, dirs_name, dirs_root_name, i_start, j_end)
    elif 23 <= dirs_name <= 45:
        j_end =12
        i_start = 4
        print("now from: " + str(i_start))
        rename(curr_dir, dirs_name, dirs_root_name, i_start, j_end)

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
                    for root, dirs, files in os.walk(curr_root):
                        for dirs_name in dirs:
                            curr_dir = os.path.join(curr_root, dirs_name)
                            rename_images(curr_dir, dirs_name, dirs_root_name)
                            # rename_images(curr_dir, dirs_name)
                            # print("curr_dir: " + str(curr_dir))
                            # print("dirs_name: " + str(dirs_name))
                            # print("dirs_root_name: " + dirs_root_name)

def main():
    # input_file_root = '/home/chloe/tensorflow/Learning-to-See-in-the-Dark/dataset/'
    # input_root = '/media/chloe/Zhu08032964448/Study/LearningToSeeInTheDark/result/visualizeImages/raw_file/'
    input_root = '/media/chloe/Zhu08032964448/Study/LearningToSeeInTheDark/result/visualizeImages/'
    get_dirs_name(input_root)

if __name__ == '__main__':
    main()