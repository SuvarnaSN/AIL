## Project Description
This project is to classify the input into 2 classes that is classify into 2 classes whether the patients will get readmitted to the hospital within 30days or not. 

## Aim 
This project is designed and implemented to forecast the patient readmission within 30days based on the dataset.

## Inputs Considered
Input Dataset 
  name = Diabetes 130-US Hospitals for Years 1999-2008
  source = ucimlrepo
Target Column in the Dataset
"NO"
0 (Not readmitted)
">30"
0 (Not readmitted within 30 days)
"<30"
1 (Readmitted within 30 days) 

## Dataset
Rows: 100,000+
 Features: Age, race, admission type, discharge, diagnosis codes, number of medications, lab procedures, number of diagnoses, etc.
 Target column: readmitted → “<30”, “>30”, “NO” → Convert into binary (yes/no for within 30 days)

## Files
HospitalReadmissionAdmission.ipynb

## Project Code Description
1. ### Loading and cleaning of input data :
   We first load the dataset (HospitalReadmissionAdmission csv) into a dataframe. Dataframe is something like a table that contains rows and columns. Every row is an observation and every column 
   represents a variable. Here we have the column which is called readmitted and it contains values >30 and <30
   
2. ###  Convert to Binary and drop unnecessary input columns:
   We find the total missing data from that readadmitted column. Then convert readmitted to binary and drop unnecessary ip columns. Check which values have missing data.

3. ###  Encode Categorical Columns :
  Find all categorical (text) columns. Convert them into numeric columns and keep the dataset model-friendly. 

4. ### Encode them using One-Hot Encoding:
   Creates a new column for each unique category fills it with 1s and 0s.
   
5. ### Split into Train/Test Sets
    Divide the data into train and test datasets. 20% for testing, 80% for training

6. ### Model Training & Evaluation
   We train using 3 algorithms 1. Logistic Regression, Random Forest and XGBoost. Out of all 3 XGBoost gave us better performance.

7. ### Visualisation
   We then visualise the comparison of the output obtained from all 3 algorithms and compare which one is better.

   
