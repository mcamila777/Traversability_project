import sys
from PIL import Image
import numpy as np
import os
import argparse
caffe_root = 'SegNet/caffe-segnet/' 			# Change this to the absolute directoy to SegNet Caffe
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Import arguments
parser = argparse.ArgumentParser()
#parser.add_argument('--model', type=str, required=True)
#parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--iter', type=int, required=True)
args = parser.parse_args()

net_path = "SegNet/Models/classifier_inference_UAO.prototxt"
caffemodel_path = "SegNet/Models/Training/1_classifier_UAO_indoor_iter_3000.caffemodel"
data_path = "imageVelDataset/all_augmented_data"



#caffe.set_mode_cpu()
caffe.set_device(0)
caffe.set_mode_gpu()


net = caffe.Net(net_path, caffemodel_path, caffe.TEST)



for i in range(0, args.iter):

	net.forward()
	#print net.blobs['data'].data.shape 

	image = net.blobs['data'].data
	label = net.blobs['label'].data
	predicted = net.blobs['prob'].data
	image = np.squeeze(image[0,:,:,:])

	print predicted

	ind = np.argmax(predicted)
	print "Label: " +str(label)
	print "predicted class: " + str(ind)

	#accuracy??????????????????????????????????????