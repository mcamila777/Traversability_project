import sys
import caffe
from PIL import Image
import numpy as np

pimga = Image.open("a.jpg")
pimgb = Image.open("b.jpg")
nimga = np.array(pimga).reshape(1,256,256,3).transpose(0,3,1,2)
nimgb = np.array(pimgb).reshape(1,256,256,3).transpose(0,3,1,2)

caffe.set_mode_cpu()
net = caffe.Net("model/net.prototxt", "model/net.caffemodel",0)
print net.forward_all(**{"data_a":nimga, "data_b":nimgb})