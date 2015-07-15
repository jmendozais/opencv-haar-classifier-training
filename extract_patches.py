import sys
import cv2
import os
import os.path as path

if len(sys.argv) < 4:
	print "Usage: extract_patches data_dir list_path out_dir"
	sys.exit()

data_dir = sys.argv[1]
list_path = sys.argv[2]
out_dir = sys.argv[3]

os.popen("rm -rf {0}; mkdir {0}".format(out_dir))

f = open(list_path)
lines = [line for line in f]
for line in lines:
	toks = line.split(' ')
	assert len(toks) == 6
	img_path = path.join(data_dir, toks[0])
	ann_path = img_path[len(img_path) - 3] + 'txt'
	out_path = path.join(out_dir, img_path.split('/')[-1])

	x = int(toks[2])
	y = int(toks[3])
	width = int(toks[4])
	height = int(toks[5])
	
	img = cv2.imread(img_path)
	roi = img[y:y+height, x:x+width]
	'''
	cv2.rectangle(roi, (x,y), (x + width, y + height), (0, 0, 255))
	cv2.imshow('bbox', roi)
	cv2.waitKey()
	'''
	cv2.imwrite(out_path, roi)
	
