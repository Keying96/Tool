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


def plot_images(curr_plot_root,dirs_root_name):
    """
    he show_size is the number of pixels to show for each image.
    The max value is 299.
    :param curr_root:
    :param dirs_root_name:
    :return:
    """

    # Initialize the array of images.
    images = []

    images_list = os.listdir(curr_plot_root)
    for item in images_list:
        image_root = os.path.join(curr_plot_root, item)IMAGE_COLUIMAGE_COLUMNMN
        # print (image_root)

        img = mpimg.imread(image_root)
        images.append(img)

    # Create figure with sub-plots.
    sum = len(images)
    w = 5.0
    h = math.ceil(sum/w)

    w = int(w)
    h = int(h)

    fig, axes = plt.subplots(w,h)

    # Adjust vertical spacing.
    # fig.subplots_adjust(left=0, bottom=0, right=1, top=1,
    #             wspace=0, hspace=0)
    # fig.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    # fig.subplots_adjust(hspace=0.1, wspace=0.1)
    # for i, ax in enumerate(axes.flat):

    for i, ax in enumerate(axes.flat):
        print("images_list: " + str(len(images_list)))
        if i <= len(images_list)-1:
            print ("i: " + str(i))

            img = images[i]
            ax.imshow(img, cmap = 'gray')
            # Remove ticks.
            ax.set_xticks([])
            ax.set_yticks([])

        # Remove ticks.
        ax.set_xticks([])
        ax.set_yticks([])

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

    # Ensure the plot is shown correctly with multiple plots
    # in a single Notebook cell.
    title = dirs_root_name
    # fig.title('images_title')
    plt.show()
    # plt.savefig('zhu_save.png')

def get_dirs_name(input_root):
    if os.path.isdir(input_root):
        for root, dirs, files in os.walk(input_root):
            for dirs_root_name in dirs:
                curr_root = os.path.join(input_root, dirs_root_name)
                if os.path.isdir(curr_root):
                    # print ("curr_root: " + curr_root)
                    # print ("dis_name: " + dirs_root_name)
                    for root, dirs, files in os.walk(curr_root):
                        for dirs_root_name in dirs:
                            curr_plot_root = os.path.join(curr_root, dirs_root_name)
                            plot_images(curr_plot_root,dirs_root_name)
                            # print (curr_plot_root)

def main():
    # input_root = '/media/chloe/Zhu08032964448/Study/Processing/'
    input_root = '/media/chloe/Zhu08032964448/Study/test/'
    get_dirs_name(input_root)


if __name__ == '__main__':
    main()