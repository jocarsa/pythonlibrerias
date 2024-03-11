import cv2
import numpy as np

image = np.zeros((400, 400, 3), dtype=np.uint8)

cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 0), thickness=2)

cv2.rectangle(image, (200, 50), (300, 150), (0, 0, 255), thickness=-1)

cv2.circle(image, (100, 300), 50, (255, 0, 0), thickness=2)

cv2.line(image, (250, 300), (350, 400), (255, 255, 0), thickness=2)


cv2.putText(image, 'OpenCV', (200, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
