# Wine-Quality-Prediction

## Objective
  The objective of this project is to predict quality of a red wine in scale of 0-10 given set of features as input..Here is a list of columns of the data set
  
  * **Fixed Acidity**
  * **Volatile Acidity**
  * **Citric Acid**
  * **Residual Sugar**
  * **Chlorides**
  * **Free Sulfur Dioxide**
  * **Total Sulfur Dioxide**
  * **Density**
  * **pH**
  * **Sulphates**
  * **Alcohol**
  * **Quality**
  
## Pre Requisites

  * Python
  * **Libraries**
    * pandas
    * sklearn
    * matplotlib
    * seaborn

## Built With

  * In this project Different models are used
    * **Naive Bayes**
    * **Decision Tree**
    * **Random Forest**
    
## Accuracy

  * **If Threshold id 0.00**
  
  |    **Models**     |  **Score**  |
  |---------------|:-------:|
  |  **Naive Bayes**  |  **56.00%** |
  | **Decision Tree** |  **64.50%** |
  | **Random Forest** |  **71.75%** |
  
  * **If Threshold is 0.05**
  
  |    **Models**     |  **Score**  |
  |---------------|:-------:|
  |  **Naive Bayes**  |  **56.75%** |
  | **Decision Tree** |  **61.75%** |
  | **Random Forest** |  **72.25%** |
  
  The Best Accuracy after predicting is when threshold is **0.05** and model is Random Forest(**73%**)
  
