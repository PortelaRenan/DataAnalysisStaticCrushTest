<div align="center">

# 🧪 Static Crush Test Data Analysis of Composite Hat Channels

**Python analysis of static crush tests on composite hat channel parts**

🎓 *Developed as part of my doctoral research in Mechanical Engineering at the University of Waterloo*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/topic-composite%20crashworthiness-blueviolet)
![Research](https://img.shields.io/badge/PhD%20research-University%20of%20Waterloo-FFC72C)
![Status](https://img.shields.io/badge/status-archive-lightgrey)

[About](#-about) · [Structure](#-repository-structure) · [Background](#-background) · [How to run](#-how-to-run) · [Citation](#-citation) · [Contact](#-contact)

</div>

---

## 📌 About

This repository contains the **Python code and test data** used to analyze **static crush tests of composite hat channel parts**. The work was developed as part of my **doctoral research in Mechanical Engineering at the University of Waterloo** (Canada).

The goal is to process the data measured in the crush tests in a **consistent and reproducible way**, so that results from different test series can be compared with each other.

<!-- Add here the research context: the material system, the manufacturing process, the test standard or setup, and the link to the thesis or papers -->

## 📂 Repository structure

```
data-analysis-static-crush/
├── crush_test.py      ← analysis script
├── [1] AT/            ← test series 1
├── [2] UNB/           ← test series 2
├── [3] VAC 20s/       ← test series 3
└── README.md
```

| Item | Description |
|---|---|
| [`crush_test.py`](crush_test.py) | Python script that processes the crush test data |
| [`[1] AT`](<[1] AT/>) | Data of test series 1 (AT) |
| [`[2] UNB`](<[2] UNB/>) | Data of test series 2 (UNB) |
| [`[3] VAC 20s`](<[3] VAC 20s/>) | Data of test series 3 (VAC 20s) |

<!-- Explain what AT, UNB and VAC 20s mean (for example, manufacturing conditions, material batches or test series) and what files each folder contains -->

## 🧠 Background

A **hat channel** is an open-section profile, with a shape similar to a hat, widely used as a structural member in vehicles. In a **static crush test**, the part is compressed at a low, constant speed, while the **force** and the **displacement** are recorded.

The resulting force-displacement curve shows how the part **absorbs energy** while it collapses, which is a key property for **crashworthiness** of lightweight composite structures.

<!--
Optionally list the quantities calculated by crush_test.py, for example:
peak crush force, mean crush force, absorbed energy, specific energy absorption (SEA), crush force efficiency
-->

<!--
## 🖼️ Results
Add the force-displacement curves and photos of the crushed parts here. Save the images in an images/ folder, for example:

| Force-displacement curves | Crushed hat channel |
|:---:|:---:|
| ![Curves](images/force_displacement.png) | ![Part](images/crushed_part.png) |
-->

## 🚀 How to run

**Requirements:** Python 3.8 or later.

**1. Clone the repository**

```bash
git clone https://github.com/PortelaRenan/data-analysis-static-crush.git
cd data-analysis-static-crush
```

**2. Install the dependencies**

```bash
pip install numpy pandas matplotlib
```

**3. Run the analysis**

```bash
python crush_test.py
```

<!-- Adjust the dependencies to the imports of crush_test.py and describe the inputs (data files, folder paths) and the outputs (plots, tables) -->

## 🛠️ Technologies

- **Python**: data processing and analysis
- **NumPy** and **pandas**: numerical computation and data handling
- **Matplotlib**: plots of the results

## 📝 Citation

If you use this code or data in your work, please cite the related publication:

```bibtex
@phdthesis{portela_thesis,
  author = {Portela, Renan},
  title  = {THESIS TITLE},
  school = {University of Waterloo},
  year   = {YEAR},
  url    = {THESIS LINK}
}
```

## 📬 Contact

**Renan Portela**, PhD in Mechanical Engineering (University of Waterloo, Canada) · Master's in Mechanical Engineering (UNICAMP)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR-PROFILE)
[![Email](https://img.shields.io/badge/E--mail-D14836?logo=gmail&logoColor=white)](mailto:YOUR-EMAIL@example.com)

---

<div align="center">

⭐ If this repository helped you, leave a star!

</div>
