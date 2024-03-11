import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    # Invert the colors
    inverted_frame = 255 - frame

    cv2.imshow('Webcam Feed (Inverted)', inverted_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
