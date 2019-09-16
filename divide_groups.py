# -*- coding:utf-8 -*-
"""
根据文件名把图片进行分组
e.g.:
    文件名: 00000_0_0.png

在图片文件夹下
"""
import  os
import filetype
import shutil

def remove_image(input_root, currdir_root, item, imagename_flag, imagelayer_flag):
    """
    e.g.: /media/chloe/Zhu08032964448/Study/Processing_raw/00000 00000_1_5.png 00000 1
    :param input_root: 整理得到图片导根目录
    :param currdir_root: media/chloe/Zhu08032964448/Study/Processing_raw/00000 (图片所在目录)
    :param item: 00000_1_5.png  (被remove对象的文件名)
    :param imagename_flag: 00000 (文件所属的图片)
    :param imagelayer_flag: 1 (文件所在的层数)
    :return:
    """
    # print (currdir_root + " " + item + " " + imagename_flag + " " +imagelayer_flag)
    save_root = os.path.join(input_root, imagename_flag)
    save_root = os.path.join(save_root, imagelayer_flag)
    input_image_path  = os.path.join(currdir_root,item)
    save_image_path = os.path.join(save_root, item)
    # print ("save_root: " + save_root)
    if not os.path.exists(save_root):
        os.makedirs(save_root)
        shutil.copy(input_image_path, save_image_path)
        print (input_image_path + "  " + save_image_path)
    else:
        shutil.copy(input_image_path, save_image_path)
        print (input_image_path + "  " + save_image_path)


def divide_group(input_root, currdir_root, dir_name):
    """
    根据文件名中的"_"符号,将得到文件的相关信息flag
    :param input_root:
    :param currdir_root:
    :param dir_name: 文件夹名
    :return:
    """
    file_list = os.listdir(currdir_root)
    for item in file_list:
        item_root = os.path.join(currdir_root, item)
        if os.path.isfile(item_root):
            kind = filetype.guess(item_root)
            try:
                if kind.extension == 'png':
                    flaglist = item.split("_")
                    if len(flaglist) == 3:
                        imagename_flag = flaglist[0]
                        imagelayer_flag = flaglist[1]
                        remove_image(input_root, currdir_root, item, imagename_flag, imagelayer_flag)
                        # print ("flaglist: " + str(flaglist))
            except:
                # raise
                print(" 'NoneType' object has no attribute 'extension'")

def get_dir_name(input_root):
    """
    得到路径下的文件夹名
    :param input_root: 输入文件目录地址
    :return: currdir_root: /media/chloe/Zhu08032964448/Study/Processing_raw/00000
    """
    if os.path.isdir(input_root):
        for root, dirs, files in os.walk(input_root):
            for dir_name in dirs:
                currdir_root = os.path.join(input_root, dir_name)
                if os.path.isdir(currdir_root):
                    divide_group(input_root,currdir_root, dir_name)
                    print ("currdir_root: " + currdir_root)

            # for file in files:
            #     currfile_root = os.path.join(input_root, file)
            #     if os.path.isfile(currfile_root):
            #         print ("currfile_root: " + currfile_root)

def main():
    # input_root = "/media/chloe/Zhu08032964448/Study/Processing_raw/"
    input_root = "/media/chloe/Zhu08032964448/Study/Processing/"
    get_dir_name(input_root)

if __name__ == '__main__':
    main()