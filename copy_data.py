import sys
import os
import os.path as path

in_dir = sys.argv[1]
in_list = sys.argv[2]
out_dir = in_list.split('.')[0]

f = open(in_list)
for line in f:
	line = line[:-1]
	img_path = line.split(' ')[0]
	img_path = path.join(in_dir, img_path)
	print 'cp {} {}'.format(img_path, out_dir)
	os.popen('cp {} {}'.format(img_path, out_dir))
