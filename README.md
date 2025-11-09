# 🌞 Solar Challenge — Data Profiling, Cleaning & EDA

**Exploratory Data Analysis (EDA) for Solar Datasets from Benin, Togo, and Sierra Leone**


---

## 🧠 Overview

This project is part of the **Solar Challenge**, focusing on understanding solar energy data collected from multiple African countries.  
It includes **Git & Environment Setup** and full **Exploratory Data Analysis (EDA)** workflows for:
- 🇧🇯 **Benin**
- 🇹🇬 **Togo**
- 🇸🇱 **Sierra Leone**

The goal is to prepare, clean, and visualize solar datasets to identify insights about irradiance, temperature, wind, and humidity patterns.

---

## 🎯 Objectives

- Initialize and manage the project with **Git and GitHub**  
- Configure a reproducible **Python environment**  
- Perform **data profiling and cleaning** for each dataset  
- Conduct **EDA** to uncover trends, correlations, and outliers  
- Automate environment verification with **GitHub Actions**

---

## 🧱 Project Structure

```
├── .github/
│   └── workflows/
│       └── ci.yml
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
├── data/
│   ├── (raw and cleaned CSV files - ignored)
├── scripts/
├── tests/
├── .gitignore
├── requirements.txt
├── README.md
└── DOCUMENTATION.md
```

---

## ⚙️ Setup & Installation (Windows)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<lidiya207>/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Verify Environment
Run the GitHub Actions workflow or manually check:
```bash
python --version
```

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
scipy
streamlit
```

Install via:
```bash
pip install -r requirements.txt
```

---

## 🔬 Data Profiling & Cleaning

Each country’s dataset underwent:
- **Summary Statistics** (`df.describe()`)
- **Missing Value Detection**
- **Outlier Identification** using Z-score
- **Median Imputation** for missing numeric data
- **Export of cleaned dataset** to `/data/<country>_clean.csv` (not pushed to GitHub)

---

## 📊 Exploratory Data Analysis (EDA)

### 📈 Time Series Analysis
- Line plots for **GHI**, **DNI**, **DHI**, and **Tamb** vs **Timestamp**
- Detects daily and monthly solar patterns.

### 🧹 Cleaning Impact
- Comparison of **ModA** and **ModB** readings before and after cleaning.

### 🔥 Correlation Analysis
- Heatmaps showing relationships between irradiance, temperature, humidity, and wind.

### 🌬️ Wind and Distribution Analysis
- Wind speed histograms and scatter plots (WS vs GHI).

### 🌡️ Temperature Analysis
- Scatter plots of **RH vs Tamb** and **RH vs GHI** to understand environmental impacts.

### 🫧 Bubble Charts
- Visualization of **GHI vs Tamb** with bubble size representing **Relative Humidity (RH)**.

---

## 🧾 Git & Workflow Summary

- **Repository Name:** `solar-challenge-week0`  
- **Main Branch:** `main`  
- **Feature Branches:** `setup-task`, `eda-benin`, `eda-togo`, `eda-sierra-leone`  

Typical workflow:
```bash
git checkout -b eda-benin
# make changes
git add .
git commit -m "feat: complete EDA for Benin dataset"
git push origin eda-benin
```
Then open a **Pull Request** to merge into `main`.

---

## 📈 Key Insights

- **GHI, DNI, and DHI** are highly correlated, peaking around midday.  
- **Outliers** were detected in sensor readings during irregular sunlight or equipment faults.  
- **Humidity** shows an inverse correlation with temperature.  
- **Wind patterns** show consistent daily variations across datasets.  

---

## ✅ Key Performance Indicators (KPIs)

| KPI | Description |
|-----|--------------|
| 🧠 Proactivity | Demonstrated independent exploration and data understanding |
| 📊 EDA Quality | Used meaningful visualizations and statistics |
| 🧹 Data Cleaning | Identified and corrected missing and anomalous data |
| 💡 Insights | Generated actionable, evidence-based observations |

---

## 👩‍💻 Author

**Lidiya Getale**  
🎓 Bahir Dar University | Software Engineering Student  
📧 [lidiyagetale774@gmail.com](mailto:lidiyagetale774@gmail.com)  
🌍 Ethiopia  

---

