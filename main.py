import numpy as np
import cv2
from mss import mss
import game_control


bbox = {'top': 270, 'left': 0, 'width': 750, 'height': 300}
roi_box = {'top': 380, 'left': 140, 'width': 150, 'height': 120}
background_sample = {'top': 880, 'left': 0, 'width': 150, 'height': 120}

sct = mss()
first_frame = None

orig_bg = sct.grab(background_sample)
orig_bg_frame = np.array(orig_bg)

while 1:
    # Checking white BG:
    curr_bg = sct.grab(background_sample)  # 1 = WHITE
    curr_bg_frame = np.array(curr_bg)

    # if curr_bg_frame[0][0][0] == orig_bg_frame[0][0][0]:

    # starting the browser if closed
    if game_control.status == 0:
        game_control.control(1)

    sct_img = sct.grab(bbox)
    roi_img = sct.grab(roi_box)
    # gray_img = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)

    #
    # mask_roi = cv2.inRange(hsv, np.array([0, 0, 0], np.array([0, 0, 0])))
    # kernel = np.ones((5, 5))
    #
    # dilation = cv2.dilate(mask_roi, kernel, iterations=1)
    #
    # erosion = cv2.erode(dilation, kernel, iterations=1)
    #
    # filtered = cv2.GaussianBlur(erosion, (3, 3), 0)


    frame = np.array(sct_img)
    roi_frame = np.array(roi_img)

    #gray_img = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(roi_frame, (3, 3), 0)
    hsv = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 0], dtype=np.uint8)
    upper = np.array([0, 0, 0], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(roi_frame, roi_frame, mask=mask)

    # show the images
    cv2.imshow("images", np.hstack([roi_img, output]))



    print("FRAME: \n", frame)
    print("ROI FRAME: \n", roi_frame)

    # Visualizing the dino & surroundings
    cv2.rectangle(frame, (30, 110), (180, 230), (0, 0, 255), 2)
    cv2.rectangle(frame, (150, 110), (220, 230), (250, 0, 0), 2)



    cv2.imshow('LIVE Show', frame)
    cv2.imshow("Hurdles", roi_frame)
   # cv2.imshow("Hurdle Contour", roi_frame_gray)

    # time.sleep(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
