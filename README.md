
# 🧹 Netflix Titles Data Cleaning Task

## 📌 Task Overview
This project was part of a data analyst internship assignment focused on cleaning and preprocessing raw data. The dataset used contains metadata about movies and TV shows available on Netflix.

---

## 📂 Dataset
**Source:** Kaggle - Netflix Movies and TV Shows  
**File Used:** `netflix_titles.csv`

---

## 🎯 Objective
To clean the raw dataset by:
- Handling missing values
- Removing duplicates
- Standardizing inconsistent formats
- Ensuring proper data types
- Creating a final version ready for analysis

---

## 🔧 Steps Performed

1. **Removed duplicates:**  
   Used `.drop_duplicates()` to ensure no redundant rows remained.

2. **Handled missing values:**  
   - Filled `director`, `cast`, and `country` with `"Unknown"`  
   - Dropped rows with missing values in critical fields like `date_added`, `rating`, and `duration`

3. **Converted data types:**  
   - Transformed `date_added` to datetime format using `pd.to_datetime()`

4. **Standardized text fields:**  
   - Converted text columns to lowercase  
   - Removed leading/trailing spaces

5. **Renamed columns:**  
   - Replaced spaces with underscores  
   - Standardized all column names to lowercase

---

## 🧰 Tools Used
- **Language:** Python  
- **Libraries:** Pandas

---

## 📁 Files Included
- `cleaned_Netflix_show.xlsx`: Final cleaned dataset  
- `cleaning_script.py`: Python code used for cleaning (if applicable)

---

## ✅ Final Output
A cleaned and consistent dataset with no missing critical values, ready for analysis or visualization.