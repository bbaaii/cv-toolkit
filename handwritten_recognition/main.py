# 作者：李可艺
# 创建于：2018-7-18
import numpy as np
import pickle
import os
import time
import sys
import shutil
import skimage


caffe_root = '~/caffe-master/'
sys.path.insert(0, caffe_root + 'python')
import caffe


net_file = 'googlenet_deploy.prototxt'
caffe_model = 'models/googlenet_hccr.caffemodel'
mean_file = 'meanfiles/CASIA1.0_1.1_1.2_mean_112.npy'
unicode_index = np.loadtxt('util/unicode_index.txt', delimiter=',', dtype=np.int)
net = caffe.Net(net_file,caffe_model,caffe.TEST)


def get_crop_image(imagepath, img_name):
    img = skimage.io.imread(imagepath + img_name, as_grey=True)
    black_index = np.where(img < 255 )
    min_x = min(black_index[0])
    max_x = max(black_index[0])
    min_y = min(black_index[1])
    max_y = max(black_index[1])

    # load image to caffe
    image = caffe.io.load_image(imagepath + "//" + img_name)
    return image[ min_x : max_x, min_y : max_y, : ]


def evaluate(imagepath, top_k):
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    transformer.set_raw_scale('data', 255)

    # for evaluation
    rightcount = 0
    allcount = 0

    allimage = os.listdir(imagepath)

    for img_name in allimage:
        allcount = allcount + 1
        label_truth = img_name.split('.')[0]

        image = get_crop_image(imagepath,img_name)
        net.blobs['data'].data[...] = transformer.preprocess('data',image)
        out = net.forward()
        label_index = net.blobs['loss'].data[0].flatten().argsort()[-1 : -top_k - 1 : -1]
        labels = unicode_index[label_index.astype(np.int)]

        # calc accuracy
        for i in range(0, top_k):
            if  labels[i] == int(label_truth):
                rightcount = rightcount + 1
            break

    return rightcount,allcount,(float)(rightcount)/(float)(allcount)


def predict(file_name):
    # crop image
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    transformer.set_raw_scale('data', 255)

    image = get_crop_image('', file_name)

    net.blobs['data'].data[...] = transformer.preprocess('data',image)

    # forward image to model
    out = net.forward()
    label_index = net.blobs['loss'].data[0].flatten().argsort()[-1:-2:-1]

    # output unicode
    labels = unicode_index[label_index.astype(np.int)]

    return labels


# unit test
if __name__=='__main__':
    imagepath='images/'
    for top_k in [1, 2, 5, 10]
        top_k = 1;
        evaluate(imagepath,top_k)
