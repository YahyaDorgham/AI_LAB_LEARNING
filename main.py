import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset = pd.read_csv("Wuzzuf_Jobs.csv")
#
# #**********************************************************************
# # Q 1,2
# x = dataset.iloc[0:5,:]
# print(x)  # display first 5 raws from dataset
# print(dataset.info) #structure of the dataset
# print(dataset.describe())  # Summary of the dataset
# #***************************************************************************
# # Q 3
# dataset.drop_duplicates(inplace=True)
# dataset.dropna(inplace=True)
# print(dataset.info) #it will be [4377 rows x 8 columns] after [4380 rows x 8 columns]
# dataset.dropna(inplace=True)  #replace missing data with true
# # *****************************************************************************
# #Q 4,5
# x = dataset.iloc[:,[1]]
# Jobs_companies = x.value_counts()[:5]
# print(Jobs_companies)
# plt.pie(Jobs_companies)
# plt.show()
#
# #*********************************************************************************
# # Q 6,7
# x = dataset.iloc[:,[0]]
# y = x.value_counts()[:10]
# print(y)
# plt.subplots(figsize=(10,10))
# y.plot.bar(color='blue',width=0.4,fontsize=10)
# plt.xlabel("job titles")
# plt.ylabel("workers")
# plt.title("most popular job titles")
# plt.show()
# #****************************************************************************************
# # Q 8,9
# x = dataset.iloc[:,[2]]
# y = x.value_counts()[:10]
# print(y)
# plt.subplots(figsize=(10,10))
# y.plot.bar(color='blue',width=0.4,fontsize=10)
# plt.xlabel("areas")
# plt.ylabel("workers")
# plt.title("most popular areas")
# plt.show()
# #*******************************************************************************************
# # Q 10
# x = dataset.iloc[:,[7]]
# y=x.value_counts()
# print(y)
