import numpy as np
import matplotlib.pyplot as plt
import os.path
import json
import scipy
import argparse
import math
import pylab
from sklearn.preprocessing import normalize
caffe_root = 'SegNet/caffe-segnet/' 			# Change this to the absolute directoy to SegNet Caffe
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--iter', type=int, required=True)
args = parser.parse_args()

caffe.set_mode_gpu()

net = caffe.Net(args.model,
                args.weights,
                caffe.TEST)

#Gobal Acc
glob_acc_accum = []

savePath = '../Traversability_project/imageVelDataset/featMapimagesOct23'

for i in range(0, args.iter):

	net.forward()

	image = net.blobs['data'].data
	label = net.blobs['label'].data
	predicted = net.blobs['prob'].data
	image = np.squeeze(image[0,:,:,:])
	output = np.squeeze(predicted[0,:,:,:])
	ind = np.argmax(output, axis=0)


	#Test 
	# print("pool1 shape", net.blobs['pool1'].data .shape)
	# print("pool2 shape", net.blobs['pool2'].data .shape)
	# print("pool3 shape", net.blobs['pool3'].data .shape)
	# print("pool4 shape", net.blobs['pool4'].data .shape)
	# print("pool5 shape", net.blobs['pool5'].data .shape)
	

	#print("image shape", image.shape)
	midlevel = net.blobs['pool5'].data

	


	
	#Save .npy array
    	fileName = os.path.join(savePath, "feat_map_%s" % (i))
    	np.save(fileName, midlevel[0,:,:,:])
	print("midlevel shape", midlevel[0,:,:,:].shape)


	

print 'Success!'

