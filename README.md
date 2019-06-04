# darknetHeadDetector
Source code to train a head detector using the darknet framework. The dataset comes from [here](https://www.di.ens.fr/willow/research/headdetection/) and it's parsed from VOC format to darknet format using convert2Yolo. This give a dataset of ~225k images. The architecture is based on the yolov3. The cfg is under headDetector/config/detectHeadInference.cfg and the weights can be downloaded [here](https://onedrive.live.com/download?cid=7C672603C5F48022&resid=7C672603C5F48022%2145379&authkey=AImJgesooJqi2kQ).

# Train instruction
`cd darknetHeadDetector`  
`make # CUDA, CUDNN, OPENCV dependencies`  
`bash headDetector/download.sh # Download data and pretrained weights`  
`bash headDetector/setup.sh`  
`./darknet detector train headDetector/config/headData.data headDetector/config/detectHead.cfg headDetector/darknet53.conv.74 > headDetector/train.log`  
  

# Test detection
`./darknet detector test headDetector/config/headData.data headDetector/config/detectHead.cfg headDetector/checkpointWeights/detectHead_58000.weights data/person.jpg -thresh 0.1337`
