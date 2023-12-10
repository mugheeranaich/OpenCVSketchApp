import cv2

image = cv2.imread("path to image")

if image is None:
    print("Error")

else:
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    inverted = 255 - gray_image

    blur = cv2.GaussianBlur(inverted,(21, 21), 0)

    inverted_blur = 255 - blur

    sketch = cv2.divide(gray_image,inverted_blur,scale=256.0)

    cv2.imwrite("sketch.png",sketch)

    cv2.imshow("sketch image",sketch)

    cv2.waitkey(0)
    cv2.destroyAllwindows()
