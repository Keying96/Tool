# -*- coding:utf-8 -*-
"""
将同一图片下同一层的所有图片放在一张图里面

2019/5/14
图像之间的间距
需要解决自动命名图像名字,和自动保存
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpimg
import math
import PIL.Image as Image

IMAGES_FORMAT = ['.jpg', '.JPG', '.PNG', '.png']  # 图片格式
# IMAGE_WIDTH = 2016
# IMAGE_HEIGHT = 1512
# IMAGE_ROW = 5  # 图片间隔，也就是合并成一张图后，一共有几行
# IMAGE_COLUMN = 4  # 图片间隔，也就是合并成一张图后，一共有几列
# input_root = '/media/chloe/Zhu08032964448/Study/test/'
input_root = '/media/chloe/Zhu08032964448/Study/Processing/'

from_image =[]
x = 0
y = 0

def plot_images(curr_plot_root,dir_layer_name,dirs_root_name):
    """
    he show_size is the number of pixels to show for each image.
    The max value is 299.
    :param curr_root:
    :param dirs_root_name:
    :return:
    """
    global from_image
    global x
    global y

    # Initialize the array of images.# 获取图片集地址下的所有图片名称
    image_names = [name for name in os.listdir(curr_plot_root) for item in IMAGES_FORMAT if
    os.path.splitext(name)[1] == item]

    # Create figure with sub-plots.
    sum = len(image_names)
    w = 10.0
    h = math.ceil(sum/w)

    IMAGE_ROW = int(w)
    IMAGE_COLUMN = int(h)
    print ("IMAGE_ROW: " + str(IMAGE_ROW) + " IMAGE_COLUMN: " + str(IMAGE_COLUMN))

    image_root = os.path.join(curr_plot_root, image_names[0])
    image = Image.open(image_root)
    IMAGE_WIDTH = image.size[0]
    IMAGE_HEIGHT = image.size[1]
    print ("IMAGE_WIDTH: " + str(IMAGE_WIDTH) +" " + "IMAGE_HEIGHT: " + str(IMAGE_HEIGHT))

    to_image = Image.new('1', (IMAGE_COLUMN * IMAGE_WIDTH, IMAGE_ROW * IMAGE_HEIGHT)) #创建一个新图

    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            # image_root = os.path.join(curr_plot_root, image_names[IMAGE_COLUMN * (y - 1) + (x - gap)])
            curr_index = IMAGE_COLUMN * (y - 1) + x - 1

            if curr_index <= sum-1 :
                print ("curr_index: " + str(curr_index))
                image_root = os.path.join(curr_plot_root, image_names[curr_index])
                # print ("image_root: " + image_root)
                fin = open(image_root)
                # from_image = Image.open(fin).resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
                from_image = Image.open(fin).resize((IMAGE_WIDTH, IMAGE_HEIGHT))
                to_image.paste(from_image, ((x - 1) * IMAGE_WIDTH, (y - 1) * IMAGE_HEIGHT))

    # print (to_image.size)
    image_save_name = str(dirs_root_name) + "_" + str(dir_layer_name) + ".png"
    IMAGE_SAVE_PATH = os.path.join(input_root, image_save_name)
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图

def get_dirs_name(input_root):
    if os.path.isdir(input_root):
        for root, dirs, files in os.walk(input_root):
            for dirs_root_name in dirs:
                curr_root = os.path.join(input_root, dirs_root_name)

                if os.path.isdir(curr_root):
                    for root, dirs, files in os.walk(curr_root):
                        for dir_layer_name in dirs:
                            print ("dir_layer_name: " + dir_layer_name)
                            curr_plot_root = os.path.join(curr_root, dir_layer_name)
                            plot_images(curr_plot_root,dir_layer_name,dirs_root_name)

def main():
    get_dirs_name(input_root)


if __name__ == '__main__':
    main()