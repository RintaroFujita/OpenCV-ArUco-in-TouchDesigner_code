import cv2
from cv2 import aruco
import numpy as np

dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
detector = aruco.ArucoDetector(dict_aruco) 

def onCook(scriptOp):
    frame = op('SRC_ANALYZE').numpyArray(delayed=True)
    scriptOp.copyNumpyArray(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = gray * 255.0
    gray = gray.astype(np.uint8)
    gray_invert = np.flipud(gray)

    corners, ids, rejectedImgPoints = detector.detectMarkers(gray_invert)

    SRC_ANALYZE_W = op('SRC_ANALYZE').width
    SRC_ANALYZE_H = op('SRC_ANALYZE').height
    aspect = SRC_ANALYZE_W / SRC_ANALYZE_H

    scr = op('script2')
    scr.lock = True
    scr.clear()
    tx = scr.appendChan('tx')
    ty = scr.appendChan('ty')
    id = scr.appendChan('id')
    scr.numSamples = len(corners)

    for i, corner in enumerate(corners):
        v = np.mean(corners[i][0], axis=0)
        tx[i] = v[0] / SRC_ANALYZE_W
        ty[i] = (-v[1] / SRC_ANALYZE_H + 1) / aspect
        id[i] = ids[i]

    scr.lock = False
    return