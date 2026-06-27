# WEEK 2 ASSIGNMENT – MODEL EVALUATION, CLASSIFICATION & MACHINE LEARNING IMPLEMENTATION 

# Team Name: Tech Nova

## Objective

The objective of this project is to understand the basics of Machine Learning by implementing **Linear Regression from Scratch** and building a **Classification Model**. These projects help us learn how machine learning algorithms make predictions and classify data.

---

## Projects Included

### 1. Linear Regression from Scratch (from Task - 2)

* Implemented using Python and NumPy.
* Calculated slope and intercept manually.
* Predicted output values.
* Calculated Mean Squared Error (MSE).
* Visualized the regression line using Matplotlib.

### 2. Classification Model (from Task - 3)

* Implemented using Logistic Regression.
* Predicted whether a student will **Pass** or **Fail** based on hours studied.
* Evaluated the model using Accuracy.

---

## Dataset

### Linear Regression

* **Dataset Used:** A small synthetic dataset created using NumPy arrays.
* **Input Feature:** Hours Studied
* **Target Variable:** Marks Scored
* This dataset was used to predict marks based on study hours.

#### Array Used

```python
X = [1, 2, 3, 4, 5, 6]
Y = [2, 4, 5, 4, 5, 7]
```

#### Table of Values Used

| Hours Studied (X) | Marks Scored (Y) |
| ----------------- | ---------------- |
| 1                 | 2                |
| 2                 | 4                |
| 3                 | 5                |
| 4                 | 4                |
| 5                 | 5                |
| 6                 | 7                |

---

### Classification

* **Dataset Used:** Student Pass/Fail dataset.
* **Input Feature:** Hours Studied
* **Target Variable:** Pass (1) / Fail (0)
* This dataset was used to classify whether a student passes or fails based on study hours.

#### Array Used

```python
X = [1, 2, 3, 4, 5, 6]
Y = [0, 0, 0, 1, 1, 1]
```

#### Table of Values Used

| Hours Studied (X) | Result (Y) |
| ----------------- | ---------- |
| 1                 | 0          |
| 2                 | 0          |
| 3                 | 0          |
| 4                 | 1          |
| 5                 | 1          |
| 6                 | 1          |

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* Scikit-learn
* Visual Studio Code / Google Colab

---

## Project Structure

```bash
Week-2-ML-Projects-TechNovas/
│
├── linear_regression.py
├── classification_model.py
├── screenshots/
│   ├── linear_regression_output_and_graph.png
│   └── classification_and_accuracy_output.png
│
└── README.md
```

---

## Screenshots

### Linear Regression Output
<img width="477" height="97" alt="Screenshot 2026-06-28 013507" src="https://github.com/user-attachments/assets/81fac169-df6d-416b-ab68-54bbeccff416" />


### Linear Regression Graph
<img width="762" height="565" alt="Screenshot 2026-06-28 013514" src="https://github.com/user-attachments/assets/db679bad-65b2-48fd-bbc7-36c50e13b8df" />


### Classification Model and Accuracy Output
<img width="252" height="66" alt="Screenshot 2026-06-28 003426" src="https://github.com/user-attachments/assets/acc1cd26-1768-4b56-9506-74faa864a938" />


---

## How to Run the Project

1. Clone or download this repository.
2. Open the project in Visual Studio Code or Google Colab.
3. Install the required libraries:

```bash
pip install numpy matplotlib scikit-learn
```

4. Run the Linear Regression program:

```bash
python linear_regression.py
```

5. Run the Classification Model:

```bash
python classification_model.py
```

6. View the output and generated graph.

---

## Repository Name

**Week-2-ML-Projects-Tech_Nova**

---

## Author

**Shan Udayan. S**

## Conclusion

This repository contains two beginner-friendly Machine Learning projects completed as part of the Week 2 assignment. The projects demonstrate the implementation of Linear Regression from Scratch and a Logistic Regression Classification Model, helping us understand the basic concepts of Machine Learning.
