# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.concatenate((data,new_record),axis=0)
age = census[:,0]

max_age = max(age)
min_age = min(age)
age_mean = np.average(age)
age_std = np.std(age)

race_0,race_1,race_2,race_3,race_4 = [],[],[],[],[]
arrays = [race_0,race_1,race_2,race_3,race_4]
for i in census[:,2]:
    arrays[int(i)].append(i)
    
len_array = [len(i) for i in arrays]

minority_race = len_array.index(min(len_array))

senior_citizens = np.array([census[i] for i in range(len(census)) if census[i,0]>60])
senior_citizens_len = len(senior_citizens)
working_hours_sum = sum([senior_citizens[i,6] for i in range(len(senior_citizens))])
avg_working_hours = working_hours_sum/senior_citizens_len

high = np.array([census[i] for i in range(len(census)) if (census[i,1]>10)])
low = np.array([census[i] for i in range(len(census)) if (census[i,1]<=10)])
avg_pay_high = np.average(high[:,7])
avg_pay_low = np.average(low[:,7])


