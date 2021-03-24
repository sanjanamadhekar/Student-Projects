# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here
# Step 1 
#Reading the file
data.head()

#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

#Plotting bar plot

plt.bar(list(data['Loan_Status'].unique()),loan_status)
plt.xlabel='Status'
plt.ylabel='count'
plt.show()

# Step 2

#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size()
  
# plot the result 
figure1 = property_and_loan.unstack().plot(kind='bar')
figure1.set(xlabel='Property Area', ylabel='Loan Status')

plt.xticks(rotation=45) 
plt.show()

# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack().plot(kind='bar',stacked=True)

#Changing the x-axis label
education_and_loan.set(ylabel='Loan Status', xlabel='Education Status')

#Rotating the ticks of X-axis

plt.xticks(rotation=45)

plt.show()

#Step 5

#Setting up the subplots
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1, figsize=(30,30)) 

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'],c='b')

#Setting the coApplicantIncomeplot axis title
ax_1.set_title('Applicant Income')

#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'],c='r')

#Setting the subplot axis title
ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Setting the subplot axis title
ax_3.set_title('Total Income')

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data['LoanAmount'],c='y')

plt.show()



