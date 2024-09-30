# Automated image pipeline for DICOM and non-DICOM images
Simple showcasing for annotating DICOM and non-DICOM images using Deep learning and Data Lake technologies

## Run
```
# Download model from Zenodo[https://zenodo.org/records/13767337]
# Edit the corresponding checkpoint path in `flask/app.py` 
docker-compose up -d
```  
Our method can be run using the following instance in docker-compose.yml:
+ S3
+ Nifi
  ![plot](./note/nifi.png)
+ Elasticsearch
+ `flask/app.py`: Our flask server (DICOM Reader & Deep learning model)

## Test annotate DICOM or PNG
1) import flask/archieve/Image Retrieve.postman_collection.json to Postman[https://www.postman.com/downloads/]
As shown in the image below, after sending a REST Request with DICOM image, the corresponding DICOM header, SNOMED prediction and confidence are returned as REST response
   ![plot](./note/postman.png)
2) open flask/send-dicom-requests.ipynb and flask/send-png-requests.ipynb with Jupyter notebook

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

## Class details
- Modalities:
|    Modality    |
|----------------|
| angiography    |
| angiography ct |
| ct             |
| mri            |
| ultrasound     |
| xray           |
| unknown        |

- IRMA codes:
|        IRMA      |
|------------------|
| 1121-110-213-700 |
| 1121-110-411-700 |
| 1121-110-414-700 |
| 1121-110-415-700 |
| 1121-115-700-400 |
| 1121-115-710-400 |
| 1121-116-917-700 |
| 1121-120-200-700 |
| 1121-120-310-700 |
| 1121-120-311-700 |
| 1121-120-320-700 |
| 1121-120-330-700 |
| 1121-120-331-700 |
| 1121-120-413-700 |
| 1121-120-421-700 |
| 1121-120-422-700 |
| 1121-120-433-700 |
| 1121-120-434-700 |
| 1121-120-437-700 |
| 1121-120-438-700 |
| 1121-120-441-700 |
| 1121-120-442-700 |
| 1121-120-451-700 |
| 1121-120-452-700 |
| 1121-120-454-700 |
| 1121-120-462-700 |
| 1121-120-463-700 |
| 1121-120-514-700 |
| 1121-120-515-700 |
| 1121-120-516-700 |
| 1121-120-517-700 |
| 1121-120-800-700 |
| 1121-120-911-700 |
| 1121-120-914-700 |
| 1121-120-915-700 |
| 1121-120-918-700 |
| 1121-120-919-700 |
| 1121-120-91a-700 |
| 1121-120-921-700 |
| 1121-120-922-700 |
| 1121-120-930-700 |
| 1121-120-933-700 |
| 1121-120-934-700 |
| 1121-120-942-700 |
| 1121-120-943-700 |
| 1121-120-950-700 |
| 1121-120-951-700 |
| 1121-120-955-700 |
| 1121-120-956-700 |
| 1121-120-961-700 |
| 1121-120-962-700 |
| 1121-127-700-400 |
| 1121-127-700-500 |
| 1121-129-700-400 |
| 1121-12f-466-700 |
| 1121-12f-467-700 |
| 1121-200-411-700 |
| 1121-210-213-700 |
| 1121-210-230-700 |
| 1121-210-310-700 |
| 1121-210-320-700 |
| 1121-210-330-700 |
| 1121-210-331-700 |
| 1121-220-213-700 |
| 1121-220-230-700 |
| 1121-220-310-700 |
| 1121-220-330-700 |
| 1121-228-310-700 |
| 1121-229-310-700 |
| 1121-230-462-700 |
| 1121-230-463-700 |
| 1121-230-911-700 |
| 1121-230-914-700 |
| 1121-230-915-700 |
| 1121-230-921-700 |
| 1121-230-922-700 |
| 1121-230-930-700 |
| 1121-230-934-700 |
| 1121-230-942-700 |
| 1121-230-943-700 |
| 1121-230-950-700 |
| 1121-230-953-700 |
| 1121-230-961-700 |
| 1121-230-962-700 |
| 1121-240-413-700 |
| 1121-240-421-700 |
| 1121-240-422-700 |
| 1121-240-433-700 |
| 1121-240-434-700 |
| 1121-240-437-700 |
| 1121-240-438-700 |
| 1121-240-441-700 |
| 1121-240-442-700 |
| 1121-320-941-700 |
| 1121-420-212-700 |
| 1121-420-213-700 |
| 1121-430-213-700 |
| 1121-430-215-700 |
| 1121-460-216-700 |
| 1121-490-310-700 |
| 1121-490-415-700 |
| 1121-490-915-700 |
| 1121-4a0-310-700 |
| 1121-4a0-414-700 |
| 1121-4a0-914-700 |
| 1121-4a0-918-700 |
| 1121-4b0-233-700 |
| 1122-220-333-700 |
| 1123-110-500-000 |
| 1123-112-500-000 |
| 1123-121-500-000 |
| 1123-127-500-000 |
| 1123-211-500-000 |
| 1124-310-610-625 |
| 1124-310-620-625 |
| 1124-410-610-625 |
| 1124-410-620-625 |

- SNOMED CT body parts:
| SNOMED CT code | Anatomical meaning        | Count | Semantic Types                       |
|----------------|---------------------------|-------|--------------------------------------|
| 113197003      | Rib                       | 80    | Body Part, Organ, or Organ Component |
| 1172006        | Dens axis                 | 37    | Body Part, Organ, or Organ Component |
| 120574008      | Upper extremity           | 2418  | Body Part, Organ, or Organ Component |
| 122494005      | cervical certebral column | 622   | Body Part, Organ, or Organ Component |
| 122495006      | Thoraric spine            | 341   | Body Part, Organ, or Organ Component |
| 122496007      | Lumbar spine              | 637   | Body Location or Region              |
| 123955006      | Thigh                     | 67    | Body Location or Region              |
| 12611008       | Tibia                     | 33    | Body Part, Organ, or Organ Component |
| 127949000      | Elbow                     | 256   | Body Location or Region              |
| 128330006      | Visual cortex             | 45    | Body Part, Organ, or Organ Component |
| 12921003       | Pelvis                    | 441   | Body Part, Organ, or Organ Component |
| 14975008       | Forearm                   | 207   | Body Part, Organ, or Organ Component |
| 16982005       | Shoulder region           | 349   | Body Location or Region              |
| 20020131       | Carpus	                   | 56    | Body Part, Organ, or Organ Component |
| 29707007       | Toe                       | 90    | Body Part, Organ, or Organ Component |
| 29836001       | Hip                       | 329   | Body Part, Organ, or Organ Component |
| 30021000       | Low extremity             | 152   | Body Part, Organ, or Organ Component |
| 32849002       | Esophageal                | 3     | Body Part, Organ, or Organ Component |
| 40983000       | Upper arm                 | 92    | Body Part, Organ, or Organ Component |
| 44567001       | Trachea                   | 9     | Body Part, Organ, or Organ Component |
| 45206002       | Nasal                     | 264   | Body Part, Organ, or Organ Component |
| 51185008       | Chest                     | 5846  | Body Location or Region              |
| 51282000       | Spine                     | 1564  | Body Part, Organ, or Organ Component |
| 51299004       | Clavicle                  | 46    | Body Part, Organ, or Organ Component |
| 53620006       | Temporomandibular joint   | 19    | Body Space or Junction               |
| 56459004       | Foot                      | 485   | Body Part, Organ, or Organ Component |
| 61685007       | Lower limb                | 2251  | Body Part, Organ, or Organ Component |
| 64234005       | Patella                   | 117   | Tissue                               |
| 70258002       | Ankle joint               | 482   | Body Space or Junction               |
| 71854001       | Colon                     | 5     | Body Part, Organ, or Organ Component |
| 72696002       | Knee region               | 674   | Body Location or Region              |
| 74670003       | Radiocarpal joint         | 218   | Body Space or Junction               |
| 7569003        | Finger                    | 345   | Body Part, Organ, or Organ Component |
| 76079001       | Joint of T12/L1           | 25    | Body Space or Junction               |
| 76752008       | Breast                    | 326   | Body Part, Organ, or Organ Component |
| 80581009       | Upper abdomen             | 37    | Body Part, Organ, or Organ Component |
| 81745001       | Eye                       | 50    | Body Part, Organ, or Organ Component |
| 818983003      | Abdominopelvic cavity     | 709   | Body Location or Region              |
| 8205005        | Wrist region              | 194   | Body Location or Region              |
| 85050009       | Humerus                   | 12    | Body Part, Organ, or Organ Component |
| 85537004       | Shoulder joint            | 134   | Body Space or Junction               |
| 85562004       | Hand                      | 1303  | Body Part, Organ, or Organ Component |
| 85856004       | Acromioclavicular joint   | 147   | Body Space or Junction               |
| 89546000       | Skull                     | 1291  | Body Part, Organ, or Organ Component |
| 91609006       | Mandible                  | 99    | Body Part, Organ, or Organ Component |
| -1             | Unknown                   | 102   | -                                    |
