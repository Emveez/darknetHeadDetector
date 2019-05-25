# darknetHeadDetector
`cd darknetHeadDetector  
make # CUDA, CUDNN, OPENCV dependencies  
bash ./headDetector/download.sh  
bash ./headDetector/setup.sh  
./darknet detector train ./headDetector/config/headData.data ./headDetector/config/detectHead.cfg ./headDetector/darknet53.conv.74 > ./headDetector/train.log  
`
* Follow train performance with darknetHeadDetector/headDetector/scripts/logCheck.sh

# Check detection
* ./darknet detector test ./headDetector/config/headData.data ./headDetector/config/detectHead.cfg ./headDetector/checkpointWeights/detectHead_500.weights data/person.jpg -thresh 0.01
