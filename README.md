# Vision & Cognative Systems

## Project Expectations From the Course

Deep Learning and Neural Networks  
<img width="1017" alt="image" src="https://user-images.githubusercontent.com/61107719/200121783-22d64a64-33d7-49f0-a9c4-3e9a5d763165.png">

Vision and Cognitive Systems
<img width="964" alt="image" src="https://user-images.githubusercontent.com/61107719/200121927-9309de72-8f39-4349-b445-f3d81aaf6db3.png">

<img width="941" alt="image" src="https://user-images.githubusercontent.com/61107719/200122045-96b5f8a5-500d-4bea-a36a-94c7809bc8ef.png">



## Daniels Proposed Game Plan:
I have found two benchmark datasets for underwater object detection.
 - ***(benchmark dataset, brackish) https://www.kaggle.com/datasets/aalborguniversity/brackish-dataset
 - (benchmark dataset, UOT32) https://www.kaggle.com/datasets/landrykezebou/uot32-underwater-object-tracking-dataset  

I have found 2 papers that use a YOLO model on these datasets
 - ***(YOLO reference paper, brackish dataset, PASCAL VOC)https://www.mdpi.com/2072-4292/13/22/4706
 - ***(YOLO reference paper, brackish dataset, UOT32)https://www.sciencedirect.com/science/article/pii/S014193312200165X

My suggestion is that we train a Py-torch faster R-CNN on the same data sets and measure the perfomance in the same way as the papers for direct comparison of the two algorythims.

Performance Monitoring  
 - mAP, mean average percision
 - Intersection over Union
 https://learnopencv.com/mean-average-precision-map-object-detection-model-evaluation-metric/
 - Frames per second. Number of images that can be analysed in a second by the trained model.

Since this has never been done before it is likely we can publish a paper on it.

## Report Template
I outlined a small plan for each section of the report to try and hit every point mentioned in the courses requirements.  
I took the nature journal latex template. It has lot of good example code for latex.  
You can edit it with this link too  
https://www.overleaf.com/8263361544xdcxdtdtshqy


## Pre-Processing Ideas  
Many of the papers I read highlighted that image pre processing is especially important for underwater object detection. Water turbulancy, impurities and light attenuation all affect the quality of the image. Preprocessing can reduce the effect of these issues. Of the 2 papers reference papers above, one does not use pre-processing and the other is very vauge about it's pre-processing. We can see if we can get a better YOLO performance than them with better pre-processing techniques. We can see what affect each preprocessing technique has on R-CNN. 

- This is an interesting program we can mention. It is not publically available so we cannot impliment it. It solves the issues of light attenuation. 
https://pub.towardsai.net/this-ai-removes-the-water-from-underwater-images-d277281bcd0f

- Histogram Attenuation Seems Like A good thing to try
https://medium.com/spidernitt/image-preprocessing-why-is-it-necessary-8895b8b08c1d

## Tutorials:
how to use pytorch for object detection   
(RCNN)
https://learnopencv.com/faster-r-cnn-object-detection-with-pytorch/

(YOLO)
https://www.section.io/engineering-education/object-detection-with-yolov5-and-pytorch/

what is yolo and all versions explained
https://www.datacamp.com/blog/yolo-object-detection-explained

## Data Sets:  
(make custom datasets from other sets) https://roboflow.com/
 - https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste
 - https://lila.science/datasets
 - (underwater animals) https://lila.science/otherdatasets#images-marine
 - (all formatts available) https://universe.roboflow.com/yoonchang-lee/marine_data/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true
 - ***(benchmark dataset, brackish) https://www.kaggle.com/datasets/aalborguniversity/brackish-dataset
 - (benchmark dataset, UOT32) https://www.kaggle.com/datasets/landrykezebou/uot32-underwater-object-tracking-dataset
 - (benchmark, looks amazing, can't find the data though) https://www.sciencedirect.com/science/article/pii/S1568494619302169
 - (non marine banchmark) https://paperswithcode.com/dataset/pascal-voc

## Relivant Scientific Literature:
 - https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.6147
 - https://www.researchgate.net/publication/349438420_Robust_ecological_analysis_of_camera_trap_data_labelled_by_a_machine_learning_model
 - (Under water object detection, overview of modern research) https://link.springer.com/article/10.1007/s11042-022-12502-1
 - (Marine Segmentation) https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=9471801&ref=aHR0cHM6Ly9pZWVleHBsb3JlLmllZWUub3JnL3NlYXJjaC9zZWFyY2hyZXN1bHQuanNwP3NlYXJjaFdpdGhpbj0lMjJQdWJsaWNhdGlvbiUyME51bWJlciUyMjo3NiZzZWFyY2hXaXRoaW49JTIyVm9sdW1lJTIyOjMyJnNlYXJjaFdpdGhpbj0lMjJJc3N1ZSUyMjo0JnNlYXJjaFdpdGhpbj0lMjJTdGFydCUyMFBhZ2UlMjI6MjMwMw==
 - (marine litter on uninhabited island) https://www.sciencedirect.com/science/article/pii/S0048969722031618
 - (review of DL marine object detection. includes list of good datasets)https://www.researchgate.net/publication/363684765_Review_on_Deep_Learning_Techniques_for_Underwater_Object_Detection
 - (YOLO reference paper, i can't find data)https://link.springer.com/content/pdf/10.1007/s11036-018-1117-9.pdf
 - ***(YOLO reference paper, brackish dataset, PASCAL VOC)https://www.mdpi.com/2072-4292/13/22/4706
 - ***(YOLO reference paper, brackish dataset, UOT32)https://www.sciencedirect.com/science/article/pii/S014193312200165X

## Other AI Conservation efforts:  
  - https://www.wildlifeinsights.org/
  - https://github.com/mikeyEcology/MLWIC2
  - https://www.conservationai.co.uk/
  - https://www.microsoft.com/en-gb/ai/ai-for-earth
  - https://www.wildme.org/codex-and-wildbook.html


Course Resources: 
<p float="left">
  <!-- <a href="https://github.com/jpazzini/MAPD-B/tree/2022/mysql" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-512.png" width="60px" />
  </a>     -->          
  <a href="https://stem.elearning.unipd.it/course/view.php?id=2920" target="_blank">
  <img src="https://tracker.moodle.org/secure/attachment/62695/Mobile-M-Icon-1-corners.png" width="60px" />
  </a>
  <a href="https://discord.gg/t6kWR5tx" target="_blank">
  <img src="https://camo.githubusercontent.com/0ef309f7e0b554033dd25b3ce83015db2f0f8952fb4c31318af095369d3d4453/68747470733a2f2f7669676e657474652e77696b69612e6e6f636f6f6b69652e6e65742f7468652d6d696e6572732d686176656e2d70726f6a6563742f696d616765732f642f64642f446973636f72642e706e672f7265766973696f6e2f6c61746573743f63623d3230313730333038303333353436" width="60px" />
  </a>
    </a>              
  <a href="https://drive.google.com/drive/folders/10seKw-qYwVETr9ps-MOcvf8-2BQZ9tv-?usp=sharing" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Google_Drive_icon_%282020%29.svg/512px-Google_Drive_icon_%282020%29.svg.png" width="60px" />
  </a>
</p>
