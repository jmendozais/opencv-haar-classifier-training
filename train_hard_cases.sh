# create positive patches in vec file
perl bin/createsamples.pl hard_cases_positives.txt negatives.txt hc_samples 5000\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
  -maxyangle 1.1 -maxzangle 1.1 -maxidev 40 -w 54 -h 40"

# create positive patches in format
# perl bin/createsamples.pl positives.txt negatives.txt samples 1500 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.1 -maxidev 40 -w 54 -h 40 -info samples/generated.txt"

python mergevec.py -v hc_samples -o hc_samples.vec

rm -rf hc_classifier
mkdir hc_classifier
opencv_traincascade -data hc_classifier -vec hc_samples.vec -bg negatives.txt\
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 3000\
  -numNeg 1800 -w 54 -h 40 -featureType HOG -mode ALL -precalcValBufSize 2048\
  -precalcIdxBufSize 2048
