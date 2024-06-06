
<p align="center">
    <h1 align="center">PARKING-DETECTION</h1>
</p>

<p align="center">
	<img src="https://img.shields.io/github/license/BeeLTL/Parking-Detection?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/BeeLTL/Parking-Detection?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/count/BeeLTL/Parking-Detection?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
 	<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
	<br>
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
</p>
<hr>

##  Quick Links

> - [ Overview](#overview)
> - [ Features](#features)
> - [ Repository Structure](#repository-structure)
> -  [ Getting Started](#getting-started)
> - [ Project contents](#project-contents)
> - [ Installation](#installation)

---

##  Overview

this is my final year master's project. It employs computer vision and machine learning to identify available parking spots in a lot, utilizing Yolov8 and ByteTrack. The system is designed to be efficient, accurate, and user-friendly.
---

##  Features

* Real-time parking spot detection
* Accurate detection of available parking spots
* Easy to use and integrate with existing parking systems
* Scalable and efficient architecture

---

##  Repository Structure

```sh
└── Parking-Detection/
    ├── LICENSE
    ├── README.md
    ├── carParking
    │   ├── detection
    │   │   │   
    │   │   ├── main.py
    │   │   └── utils
    │   │       │   ├── extract_bounding_boxes.cpython-39.pyc
    │   │       │   ├── info_drawer_utils.cpython-39.pyc
    │   │       │   └── spot_statuses.cpython-39.pyc
    │   │       ├── detect_car.py
    │   │       ├── extract_bounding_boxes.py
    │   │       ├── info_drawer_utils.py
    │   │       ├── prepare_mask.py
    │   │       └── spot_statuses.py
    │   ├── templates
    │   │   ├── index.html
    │   │   └── layout.html
    │   ├── tools
    │   │   ├── cvat annotations
    │   │   │   ├── parking1.png
    │   │   │   └── parking2.png
    │   │   ├── mask1.png
    │   │   └── mask2.png
    │   ├── videos
    │   │   ├── parking1.mp4
    │   │   └── parking2.mp4
    │   └── views.py
    ├── carParking.pyproj
    ├── carParking.pyproj.user
    ├── carParking.sln
    ├── requirements.txt
    ├── runserver.py
    └── yolov8n.pt
```


---

##  Project contents
* `main.py` : The entry point to our app.
* `prepare_mask.py` : A script designed to generate a binary mask from the mask generated through the utilization of CVAT.
* `detect_car.py` : This script detects whether a parking spot is occupied or vacant.
* `extract_bounding_boxes.py` : Takes as input our binary mask images/mask.png and generates a list detailing the bounding boxes encompassing all parking spots.
* `info_drawer_utils.py` : Utilities for drawing information.
* `spot_statuses.py` : Handles the statuses of parking spots.
---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.9`

###  Installation

1. Clone the Parking-Detection repository:

```sh
git clone https://github.com/BeeLTL/Parking-Detection
```

2. Change to the project directory:

```sh
cd Parking-Detection
```

###  Running Parking-Detection
```sh
Open carParking.sln in Visual Studio 2022
```


---





##  Resources

* `Model` : https://huggingface.co/mshamrai/yolov8x-visdrone
* `Dataset` : https://github.com/VisDrone/VisDrone-Dataset


---



