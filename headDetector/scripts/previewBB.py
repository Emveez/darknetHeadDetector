import cv2
import os
from random import shuffle

'''
	Preview the bb of the images

'''
def parsetxt(t):

	boxes = []

	with open(t) as fp:  
		line = fp.readline()
		cnt = 1
		while line:
			l = "{}".format(line.strip())
			bb = l.split(" ")
			line = fp.readline()
			cnt += 1
			bb = [float(x) for x in bb]
			boxes.append(bb[1:])

	return boxes


def main():

	txtFiles = "./labels/"
	jpegFiles = "./JPEGImages/"

	files = os.listdir(txtFiles)
	shuffle(files)


	for f in files:
		i = jpegFiles + f[:-4] + ".jpg"

		txt = txtFiles + f

		bb = parsetxt(txt)

		im = cv2.imread(i)

		imH = im.shape[0]
		imW = im.shape[1] 

		for b in bb:

			w = int(b[2] * imW) # Width of bb
			h = int(b[3] * imH) # Hight of bb

			x1 = int(b[0] * imW - w/2.0)
			y1 = int(b[1] * imH - h/2.0)

			x2 = x1 + w
			y2 = y1 + h

			cv2.rectangle(im, (x1, y1), (x2, y2), (255,0,0), 2)

		print f
		cv2.imshow("Image", im)
		a = cv2.waitKey(0)

		if a == 27:
			break

	cv2.destroyAllWindows()



if __name__ == '__main__':
	main()