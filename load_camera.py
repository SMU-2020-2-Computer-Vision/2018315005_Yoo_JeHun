import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if ret is False:
        print('Error: No image is captured!')
        break

    cv2.imshow("Video Frame", frame)
    key = cv2.waitkey(0)

    if key == 27: break
