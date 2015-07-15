from os import listdir
from os.path import isfile, join
import numpy as np
import math
import cv2
import sys

def get_paths(root, suffix = 'jpg'):
	paths = []
	for doc in listdir(root):
		file_path = join(root, doc)
		if len(doc) > len(suffix):
			name_len = len(file_path)
			if (isfile(file_path) and (file_path[name_len - len(suffix):name_len] == suffix)):                
				paths.append(join(root, doc))
	return paths

if len(sys.argv) < 2:
	print "Usage ./mean_dims data_dir"
	sys.exit()

paths = get_paths(sys.argv[1])
meanx = 0
meany = 0
for pt in paths:
	img = cv2.imread(pt)
	print img.shape
	size = img.shape
	meanx += size[0]
	meany += size[1]

print "({}, {})".format(meanx * 1.0 / len(paths), meany * 1.0 / len(paths))
