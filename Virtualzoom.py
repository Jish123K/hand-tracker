import cv2

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands

# Input from webcam

cap = cv2.VideoCapture(0)

cap.set(3, 1280)

cap.set(4, 720)

# initialize hand detector module

with mp_hands.Hands(min_detection_confidence=0.8, max_num_hands=2) as hands:

    distStart = None

    zoom_range = 0

    cx, cy = 500, 500

    # loop

    while cap.isOpened():

        success, image = cap.read()

        if not success:

            break

        # flip the image horizontally for a later selfie-view display

        image = cv2.flip(image, 1)

        # Convert the BGR image to RGB.

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # To improve performance, optionally mark the image as not writeable to pass by reference.

        image.flags.writeable = False

        # Detect hands in the image.

        results = hands.process(image)

        # Draw the hand annotations on the image.

        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Image to be zoomed

        new_img = cv2.imread('resized_test.jpg')

        if results.multi_hand_landmarks:

            # print("Start Zoom...")

            # print(handDetector.fingersUp(hands[0]))

            # print(handDetector.fingersUp(hands[1]))

            #

            if len(results.multi_hand_landmarks) == 2 and results.multi_handedness[0].classification[0].label == "Right" and results.multi_handedness[1].classification[0].label == "Left":

                # print("Start Zoom...")

                lmList1 = results.multi_hand_landmarks[0].landmark

                lmList2 = results.multi_hand_landmarks[1].landmark

                # point 8 is tip of the index finger

                if distStart is None:

                    # length, info, img = handDetector.findDistance(lmList1[8], lmList2[8], img)

                    # draw the connection points between right hand index and thum finger to left hand

                    length = (((lmList1[8].x - lmList2[8].x)**2 + (lmList1[8].y - lmList2[8].y)**2 + (lmList1[8].z - lmList2[8].z)**2)**0.5)*1000

                    # print(length)

                    distStart = length

                # length, info, img = handDetector.findDistance(lmList1[8], lmList2[8], img)

                length = (((lmList1[8].x - lmList2[8].x)**2 + (lmList1[8].y - lmList2[8].y)**2 + (lmList1[8].z - lmList2[8].z)**2)**0.5)*1000

                # info gives center x and center y

                # calculate the zoom range

                zoom_range = int((length - distStart) // 2)

                # calculate the center point so that we can  place the zooming image at the center

                cx, cy = int((lmList1[8].x + lmList2[8].x)*320), int((lmList1[8].y + lmList2[8].y
else:

    distStart = None

try:

    h, w, _ = new_img.shape

    # new height and new width

    newH, newW = ((h + zoom_range) // 2) * 2, ((w + zoom_range) // 2) * 2

    new_img = cv2.resize(new_img, (newW, newH))

    # we want the zooming image to be center and place it approx at the center

    img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = new_img

except:

    pass

# display output

cv2.imshow('output', img)

cv2.waitKey(1)


