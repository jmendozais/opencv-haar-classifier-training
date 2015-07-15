# create positive patches in vec file
perl bin/createsamples.pl hard_cases_positives.txt negatives.txt samples 1500\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
  -maxyangle 1.1 -maxzangle 0.1 -maxidev 40 -w 54 -h 40"

# create positive patches in format
# perl bin/createsamples.pl positives.txt negatives.txt samples 1500 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.1 -maxidev 40 -w 54 -h 40 -info samples/generated.txt"

python mergevec.py -v samples -o samples.vec

opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt\
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000\
  -numNeg 600 -w 54 -h 40 -featureType HOG -mode ALL -precalcValBufSize 1024\
  -precalcIdxBufSize 1024
