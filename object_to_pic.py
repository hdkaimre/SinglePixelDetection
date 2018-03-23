__author__ = 'HansDaniel'
import numpy as np
import cv2
import ThorLabMeter as tlm
import MatrixGenerator as mg

#Creates a list of masks as matrices
N=128
images = mg.matrix_list(N,128)


#installing the power meter
deviceName=input("Sisesta seadme nimi:")
power_meter=tlm.setUp(deviceName)


intensity_count=list()  #creating a list to save intensity counts

#Showing different masks and saving the reading of the intensity meter
for img in images:
    img=np.multiply(img,255)
    img = img.astype(np.uint8)
    img = cv2.resize(img, (0,0), fx=5, fy=5)
    cv2.imshow('image',img)
    cv2.waitKey(50)
    intensity_count.append(power_meter.read)
    cv2.waitKey(50)


#weighing masks with results from the intensity meter
weighed_images=list()
for i in range(0,len(intensity_count)):
    weighed_images.append(np.multiply(images[i],intensity_count[i]))

#computing the average picture
result = weighed_images[0]
for img in weighed_images:
    result = np.add(result,img)

max_intensity=result.max()
calibrated_result=np.multiply(result,255/max_intensity)
cv2.imwrite('Object.png',calibrated_result)



