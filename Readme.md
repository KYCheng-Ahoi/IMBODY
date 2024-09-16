# Automated image pipeline for DICOM and non-DICOM images
Simple showcasing for annotating DICOM and non-DICOM images using Deep learning and Data Lake technologies

## Run
- docker-compose up -d
  
Our method can be run using the following Python files:
+ `method.py`: Our method (DC3)
+ `baseline_nn.py`: Simple deep learning baseline (NN)
+ `baseline_eq_nn.py`: Supervised deep learning baseline with completion (Eq. NN)
+ `baseline_opt.py`: Traditional optimizers (Optimizer)
![plot](./note/nifi.png)

## Test
1) import flask/archieve/Image Retrieve.postman_collection.json to Postman[https://www.postman.com/downloads/]
2) open flask/send-dicom-requests.ipynb and flask/send-png-requests.ipynb with Jupyter notebook

## Dependencies within 

+ Python 3.x
+ [PyTorch](https://pytorch.org) >= 1.8
+ numpy/scipy/pandas

---------
## Contact
Ka Yung Cheng - mail@kayungcheng.de

## Publication 
[Journal] (https://www.csbj.org/article/S2001-0370(24)00203-4/fulltext)
```
@article{article,
author = {Cheng, Ka and Lange-Hegermann, Markus and Hövener, Jan-Bernd and Schreiweis, Björn},
year = {2024},
month = {06},
pages = {},
title = {Instance-level Medical Image Classification for Text-based Retrieval in a Medical Data Integration Center},
volume = {24},
journal = {Computational and Structural Biotechnology Journal},
doi = {10.1016/j.csbj.2024.06.006}
}
```
The ROCO dataset in Experiment I can be obtained from a public repository at [https://github.com/razorx89/roco-dataset], while the IRMA2007 dataset in Experiment II is available at [http://publications.rwth-aachen.de/]. Additionally, the customized SNOMED dataset utilized in Experiment III is accessible through the following URL: [https://doi.org/10.57892/100-29] and the UNIFESP dataset can be accessed through Kaggle at [https://www.kaggle.com/datasets/felipekitamura/unifesp-xray-bodypart-classification]

[Poster](https://mi-ki.eu/wp-content/uploads/2022/06/Image_Retrieve_Poster_Cheng.pdf)
```
@article{article,
author = {Cheng, Ka and Pazmino, Santiago and Bergh, Björn and Lange-Hegermann, Markus and Schreiweis, Björn},
year = {2024},
month = {01},
pages = {1388-1389},
title = {An Image Retrieval Pipeline in a Medical Data Integration Center},
volume = {310},
isbn = {9781643684567},
journal = {Studies in health technology and informatics},
doi = {10.3233/SHTI231208}
}
```
