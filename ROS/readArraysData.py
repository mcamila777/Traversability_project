import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from os.path import expanduser

camSavePath = os.path.join(expanduser("~"),'Traversability_project/imageVelDataset/imagesOct18')
velSavePath = os.path.join(expanduser("~"),'Traversability_project/imageVelDataset/velOct18')

camTimeStampArray = np.load(os.path.join(camSavePath, "camTimeStampArray.npy"))
velTimeStampArray = np.load(os.path.join(velSavePath, "velTimeStampArray.npy"))


print("velTimeStampArray Shape", velTimeStampArray.shape)
print("camTimeStampArray Shape", camTimeStampArray.shape)

print("velTimeStampArray", velTimeStampArray)
#print("velTimeStampArray last ", velTimeStampArray[-1])
print("camTimeStampArray init ", camTimeStampArray[0])
print("camTimeStampArray last ", camTimeStampArray[-1])

for i in range(1,10):
	#print Vel
	velFileName =  os.path.join(velSavePath, "vel_%s.npy" % (i))
	vel = np.load(velFileName)
	#print("Vel:" , vel)

	camFileName =  os.path.join(camSavePath, "image_%s.npy" % (i))
	image = np.load(camFileName)
	#print(image.shape)

	#Show image
	#plt.imshow(image[:,:,::-1])
	#plt.show()
	


