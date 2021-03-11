# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)


banks = bank.drop('Loan_ID',axis=1)

bank_mode = banks.mode()

for column in banks.columns:
    banks[column].fillna(bank_mode[column][0], inplace=True)


banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values=['LoanAmount'], aggfunc='mean')


loan_approved_se = banks[banks['Self_Employed']=='Yes'][banks['Loan_Status']=='Y'].shape[0]
loan_approved_nse = banks[banks['Self_Employed']=='No'][banks['Loan_Status']=='Y'].shape[0]
percentage_se = round(loan_approved_se/6.14,2)
percentage_nse = round(loan_approved_nse/6.14,2)
print(percentage_se,percentage_nse)


loan_term = banks['Loan_Amount_Term']/12
big_loan_term = loan_term[loan_term>=25].count()
big_loan_term


loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()


