import cv2


# image information
def read_image(filename, flags):
    img = cv2.imread(filename, flags)
    row = len(img)
    col = len(img[0])
    chn = len(img[0][0])
    return img, row, col, chn
