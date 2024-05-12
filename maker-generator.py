import cv2
from cv2 import aruco
import os

dir = r'assets/'
num_mark = 35
size_mark = 100


def onOffToOn(channel, sampleIndex, val, prev):
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    for id in range(num_mark):
         img_mark = aruco.generateImageMarker(dictionary, id, size_mark)

         if id < 10:
            img_name_mark = 'mark_id_0' + str(id) + '.jpg'
         else:
             img_name_mark = 'mark_id_' + str(id) + '.jpg'

         path_mark = os.path.join(dir, img_name_mark)

         cv2.imwrite(path_mark, img_mark)
    return
