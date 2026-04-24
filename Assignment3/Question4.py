#Q4. Dataset Understanding (Titanic Dataset)

#Context: First step in ML pipeline is dataset inspection.

#Dataset: Titanic (Seaborn)

import seaborn as sns
titanic = sns.load_dataset("titanic")
# Tasks:

# 1. Display:
print(titanic.head())
print(titanic.tail())
print(titanic.info())
print(titanic.describe())
# 2. Identify:
print(titanic.isnull().sum())
print(titanic.select_dtypes(include=['float64', 'int64']).columns)
print(titanic.select_dtypes(include=['object']).columns)
# 3. Explain:
# Why identifying feature types is important before modeling