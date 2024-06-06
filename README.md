
<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">PARKING-DETECTION</h1>
</p>
<p align="center">
    <em>HTTP error 404 for prompt `slogan`</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/BeeLTL/Parking-Detection?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/BeeLTL/Parking-Detection?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/BeeLTL/Parking-Detection?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/BeeLTL/Parking-Detection?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat&logo=SciPy&logoColor=white" alt="SciPy">
	<img src="https://img.shields.io/badge/SymPy-3B5526.svg?style=flat&logo=SymPy&logoColor=white" alt="SymPy">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running Parking-Detection](#-running-Parking-Detection)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

Parking-Detection is a system that uses computer vision and machine learning to detect available parking spots in a parking lot using Yolov8. The system is designed to be efficient, accurate, and easy to use.

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
    │   │       ├── __pycache__
    │   │       │   ├── detect_car.cpython-39.pyc
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

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running Parking-Detection

Open:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/BeeLTL/Parking-Detection/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/BeeLTL/Parking-Detection/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/BeeLTL/Parking-Detection/issues)**: Submit bugs found or log feature requests for Parking-detection.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/BeeLTL/Parking-Detection
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---

