## Project Description
This project is to forecast electricity consumption for the future time using the past data provided. Processes like Data Loading, Data Preprocessing, Visualisation of historical input data, Model implementation for forecasting future electricity consumption, Generation of future forecast data, Visualisation of the data generated.

## Aim 
This project is designed and implemented to forecast the electricity consumption in the upcoming future based on the usage recorded in the past.

## Inputs Considered
Input Dataset 
  name = electricityConsumptionAndProductioction
  source = Kaggle

## Files
Project1.ipynb

## Project Code Description
1. ### Loading and cleaning of input data :
   We first load the dataset (electricityConsumptionAndProductioction csv) into a dataframe. Dataframe is something like a table that contains rows and columns. Every row is an observation and every column 
   represents a variable.In this case Consumption.
   
2. ###  Pre-processing of input data after loading:
   After pre-processing of input data, we convert the date column into a datetime object.

3. ###  Set the object as an index:
   Converting the date time object into an index is important because this allows us to perform time based operations on that object like slicing the data based on date ranges is possible. Another advantage of 
   setting the date time object as an index is that it allows resampling. This means changing the data frequency. Example of this could be that if the current time frame of the input data is on hourly basis then 
   it can be adjusted in such a way that the data shown is on day-to-day basis. This is called downsampling. Both downsampling and upsampling is possible.

4. ### Visualization of data
   Plotting the line plot of Consumption trend over a period of time.
   
6. ### We check for stationarity of the data
    Stationarity means being constant over time. This is mainly checked for statistical properties of data like mean, median and variance. This needs to be checked for models like ARIMA. ARIMA stands for     
    AutoRegressive Integrated Moving Average. We need stationarity because ARIMA models assumes that the timeseries data is stationary and needs input it that manner. Stationarity means that the mean, variance,      trends are constant over time.
   
7. ### Electricity Consumption Observation and Forecasting
  We first check if the input data is stationary by running a test called ADF (Augmented Dickey Fuller test). This test is performed in timeseries and enables us to check if there is a unit root (timeseries        properties like mean, variance etc not being stationary) in the input data. In simple words, it checks if the parameters of time series data is not stationary at any point measured over time in the input data 
  provided.

  There are 2 scenarios. 
  1. Data being non-stationary which is also called null hypothesis.
  2. Data being stationary which is also called alternative hypothesis.

 We need to do this test to make sure that the data is stationary. If we make sure that the parameters are stationary this means that we can use the past records in this case electricity consumption of the past 
 to predict the future electricity consumption.

   Output of ADF Statistic
   1. #### ADF Statistic : 
        The more negative the value of ADF Statistic is, the data then it more likely to be stationary.
   2. #### p-value :
        If value of p if this is less than or equal to 0.05, then we can state that the data is stationary. If greater then non-stationary.
      
   3. #### Critical Values :
        These are thresholds that are present at different levels example 1% , 5% and 10%. If critical value is higher than ADF Statistic and ADF Statistic value is more less towards the negative, then we ignore that the parameters were non-stationary at that level.

![image](https://github.com/user-attachments/assets/bc315687-18cb-4ee7-a472-ae21e0aff6ee)
![image](https://github.com/user-attachments/assets/f05b756f-1b93-4b69-8db5-7b7f7f83eac3)

 
  



