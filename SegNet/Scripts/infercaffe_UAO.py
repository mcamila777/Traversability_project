import sys
from PIL import Image
import numpy as np
import os
import argparse
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

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
caffemodel_path = "SegNet/Models/Training/4_classifier_UAO_indoor_iter_150000.caffemodel"
data_path = "imageVelDataset/all_augmented_data"



#caffe.set_mode_cpu()
caffe.set_device(0)
caffe.set_mode_gpu()


net = caffe.Net(net_path, caffemodel_path, caffe.TEST)

y_test, y_predicted = [] , []

for i in range(0, args.iter):

	net.forward()
	#print net.blobs['data'].data.shape 

	image = net.blobs['data'].data
	label = net.blobs['label'].data
	predicted = net.blobs['prob'].data
	image = np.squeeze(image[0,:,:,:])
	ind = np.argmax(predicted)

	# print "Label: " +str(label)
	# #print "predicted class: " + str(ind)
	# #Show image
	# image = image/255.0
	# image = np.transpose(image, (1,2,0))
	# image = image[:,:,(2,1,0)]	
	# plt.figure()
	# plt.imshow(image)
	# plt.show()

	#Acum predictions and labels
	y_test.append(int(label[0]))
	y_predicted.append(ind)

#print y_test
print "accuracy_score: " + str(accuracy_score(y_test, y_predicted))
cm = confusion_matrix(y_test, y_predicted)
print "confusion_matrix: \n" + str(cm)
cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print "Normalized confusion_matrix: \n" + str(cm)




