import cv2

import mediapipe as mp

# Input from webcam

cap = cv2.VideoCapture(0)

cap.set(3, 1280)

cap.set(4, 720)

# initialize hand detector module with some confidence

mpHands = mp.solutions.hands

hands = mpHands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

# loop

while True:

    # Read the frames from webcam

    success, img = cap.read()

    

    # Convert the image to RGB format

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    

    # Detect the hands in the image

    results = hands.process(imgRGB)

    

    # Draw landmarks on the hands

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            

    # Show the output

    cv2.imshow("Sample Mediapipe output", img)

    cv2.waitKey(1)

    

# Release the capture and destroy all windows

cap.release()

cv2.destroyAllWindows()

