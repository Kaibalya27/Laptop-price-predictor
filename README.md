# Laptop-price-predictor
## Table of contents
* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Data Set](#data-set)
* [File Description](#file-description)
* [System Methodology](#system-methodology)
* [Usage](#usage)
* [Contact](#contact)
## Introduction
* This project introduces a Web Based Appliaction system designed to predict laptop prices using supervised machine learning techniques. The study employs a random decision forest as the predictive model, achieving a precision of Lorem% in price estimation.

* In this approach, the random decision forest utilizes several independent variables to predict a single dependent variable: the laptop price. The model compares actual and predicted values to assess the accuracy of its predictions.

* The project proposes a method where the price of a laptop, the dependent variable, is forecasted based on factors such as the laptop Company,Type,Inches,Screen Resoution, RAM size, weight,storage type (HDD/SSD), GPU Brand, CPU Brand, IPS ,Operating System and whether it includes a touch screen.
<p align="center">
  <img src="https://cdn.thewirecutter.com/wp-content/media/2024/07/businesslaptops-2048px-233284-2x1-1.jpg?width=2048&quality=75&crop=2:1&auto=webp" alt="Example Image" width="400"/>
</p>


## Problem Statement
<p align="center">
  <img src="https://github.com/user-attachments/assets/8e4f5d0c-ec78-43a6-bb0c-65e6a8a4bad8" alt="Alt Text" width="750" />
</p>

## Data Set
The dataset utilized in this project is 'laptop_data.csv', which includes details about laptop's different features such as brand, screen size, processor, RAM, storage, and price. It comprises 1303 rows and 12 columns. The dataset underwent significant data preprocessing, feature engineering,Exploratory Data Analysis (EDA) for analysis and for machine learning it utilizes random decision forest as the predictive model. 

## File Description
**Laptop_price_prediction.ipynb** - This Jupyter notebook contains the complete code for this project including data preprocessing, EDA, feature engineering, model building, and evaluation.

**app.py** is the primary Python script that contains the main application logic.

**df.pkl** - Pickle file of the processed data used in the model.

**pipe.pkl** - Pickle file of the machine learning pipeline used in the model.

**laptop_data.csv** - The dataset used in this project.

**requirements.txt** is a file used to list dependencies for the project.

## System Methodology

<p align="center">
  <img src="https://github.com/user-attachments/assets/62ebbe60-4f1f-4d4d-bbce-7be7ee192be0" alt="Alt Text" width="750" />
</p>

## Usage
To use the laptop price predictor, follow these instructions:

1.Copy the URL link provided below and paste it into your browser to access the webpage.

```
https://laptop-price-predictor-1-teve.onrender.com
```

2.Input the specifications of the laptop for which you want to estimate the price.
3.The system will utilize the trained model to calculate and display the predicted price.

## Contact
If you have any inquiries or encounter any issues, feel free to reach out at example@email.com. Our support team is here to assist you and ensure you have a smooth experience. Don't hesitate to contact us with any concerns or feedback.





















