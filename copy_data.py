import sys
import os
import os.path as path

in_dir = sys.argv[1]
in_list = sys.argv[2]
out_dir = in_list.split('.')[0]

f = open(in_list)
for line in f:
	img_path = line.split(' ')[0]
	img_path = path.join(in_dir, img_path)
	os.popen('cp {} {}/'.format(img_path, out_dir))
