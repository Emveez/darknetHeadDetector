# darknetHeadDetector
Source code to train a head detector using the darknet framework. The dataset comes from [here](https://www.di.ens.fr/willow/research/headdetection/) and it's parsed from VOC format to darknet format using convert2Yolo. This give a dataset of ~225k images. For fast inference the yolov3-tiny architecture is used. 

# Train instruction
`cd darknetHeadDetector`  
`make # CUDA, CUDNN, OPENCV dependencies`  
`bash ./headDetector/download.sh # Download data and pretrained weights`  
`bash ./headDetector/setup.sh`  
`./darknet detector train ./headDetector/config/headData.data ./headDetector/config/detectHead.cfg ./headDetector/darknet53.conv.74 > ./headDetector/train.log`  
  

# Test detection
`./darknet detector test ./headDetector/config/headData.data ./headDetector/config/detectHead.cfg ./headDetector/checkpointWeights/detectHead_500.weights data/person.jpg -thresh 0.1337`
