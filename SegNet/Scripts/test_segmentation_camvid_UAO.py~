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

savePath = '../Traversability_project/Segmentation_data/examp_feat_maps'

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
	

	print("image shape", image.shape)
	midlevel = net.blobs['pool5'].data
	#print("midlevel", midlevel)

	
	#Save .npy array
    	fileName = os.path.join(savePath, "feat_map_%s" % (i))
    	np.save(fileName, midlevel)


	#Example Feature map--------------
	feat_mp = midlevel[0,0,:,:]
	print("feat_mp shape", feat_mp.shape)

	#plotting------------------
	plt.figure()
	plt.imshow(feat_mp, vmin=0, vmax=1)

	#-------------------------

	r = ind.copy()
	g = ind.copy()
	b = ind.copy()
	r_gt = label.copy()
	g_gt = label.copy()
	b_gt = label.copy()

	Obstacles = [225, 13, 0]
	path_robot = [149, 255, 0]
	background = [255, 255, 255]


	label_colours = np.array([Obstacles, path_robot, background])
	for l in range(0,label_colours.shape[0]):
		#Colour all the pixels corresponding with each class at the same time
		r[ind==l] = label_colours[l,0]
		g[ind==l] = label_colours[l,1]
		b[ind==l] = label_colours[l,2]
		r_gt[label==l] = label_colours[l,0]
		g_gt[label==l] = label_colours[l,1]
		b_gt[label==l] = label_colours[l,2]


	rgb = np.zeros((ind.shape[0], ind.shape[1], 3))
	rgb[:,:,0] = r/255.0
	rgb[:,:,1] = g/255.0
	rgb[:,:,2] = b/255.0
	rgb_gt = np.zeros((ind.shape[0], ind.shape[1], 3))
	rgb_gt[:,:,0] = r_gt/255.0
	rgb_gt[:,:,1] = g_gt/255.0
	rgb_gt[:,:,2] = b_gt/255.0

	#Transformation to recover original image
	image = image/255.0

	image = np.transpose(image, (1,2,0))
	output = np.transpose(output, (1,2,0))
	image = image[:,:,(2,1,0)]


	#Accuracy

	diff =  rgb_gt-rgb
	#Round to integer all the pixels values to consider the little differences between pixels negligible
	r,c,l = diff.shape

	#diff = np.rint(diff)
	#percent = 100.*(np.where(diff == 0)[0].shape[0])/(r*c*l)

	#consider zero numbers under 1e-05
	percent = 100.*(np.where((diff == 0) | (abs(diff)<1e-05))[0].shape[0])/(r*c*l)

	
	print("Percentage of accuracy: " , percent)
	glob_acc_accum.append(percent)


	# 	#Plotting
	plt.figure()
	plt.imshow(image,vmin=0, vmax=1)
	# plt.figure()
	# plt.imshow(rgb_gt,vmin=0, vmax=1)
	# plt.figure()
	# plt.imshow(rgb,vmin=0, vmax=1)
	plt.show()


print 'Success!'
glob_acc = 0.0
print("len(glob_acc_accum) " , len(glob_acc_accum))
glob_acc = sum(glob_acc_accum)/len(glob_acc_accum)
print("Global accuracy: " , glob_acc)
