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

    scr2 = op('script2')
    scr2.lock = True
    scr2.clear()
    tx = scr2.appendChan('tx')
    ty = scr2.appendChan('ty')
    id = scr2.appendChan('id')
    scr2.numSamples = len(corners)

    for i, corner in enumerate(corners):
        v = np.mean(corners[i][0], axis=0)
        tx[i] = v[0] / SRC_ANALYZE_W
        ty[i] = (-v[1] / SRC_ANALYZE_H + 1) / aspect
        id[i] = ids[i]

    scr2.lock = False

    scr3 = op('script3')
    scr3.lock = True
    scr3.clear()
    x1 = scr3.appendChan('x1')
    y1 = scr3.appendChan('y1')
    x2 = scr3.appendChan('x2')
    y2 = scr3.appendChan('y2')
    x3 = scr3.appendChan('x3')
    y3 = scr3.appendChan('y3')
    x4 = scr3.appendChan('x4')
    y4 = scr3.appendChan('y4')
    id = scr3.appendChan('id')

    scr3.numSamples = len(corners)

    for i, corner in enumerate(corners):
        x1[i] = corner[0][0][0] / SRC_ANALYZE_W
        y1[i] = (-corner[0][0][1] / SRC_ANALYZE_H + 1) / aspect
        x2[i] = corner[0][1][0] / SRC_ANALYZE_W
        y2[i] = (-corner[0][1][1] / SRC_ANALYZE_H + 1) / aspect
        x3[i] = corner[0][2][0] / SRC_ANALYZE_W
        y3[i] = (-corner[0][2][1] / SRC_ANALYZE_H + 1) / aspect
        x4[i] = corner[0][3][0] / SRC_ANALYZE_W
        y4[i] = (-corner[0][3][1] / SRC_ANALYZE_H + 1) / aspect
        id[i] = ids[i]

    scr3.lock = False

    return