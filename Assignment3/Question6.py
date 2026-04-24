#Q6. Handling Missing Data (Critical ML Step)

#Context: Models cannot handle null values.

#Dataset: Titanic
import seaborn as sns
titanic_df = sns.load_dataset("titanic")
print(titanic_df.isnull().sum())
#Tasks:

#1. Fill missing age using median
print(titanic_df['age'].fillna(titanic_df['age'].median(), inplace=True))


#2. Fill missing embarked using mode
print(titanic_df['embarked'].fillna(titanic_df['embarked'].mode()[0], inplace=True))

#3. Drop deck column
titanic_df.drop('deck', axis=1, inplace=True)
print(titanic_df.isnull().sum())
#4. Explain:
#Different strategies are used for different columns based on the nature of the data.
#For numerical columns like age, using the median is effective as it is robust to outliers.
#For categorical columns like embarked, the mode is used to fill missing values with the most common category.
#Dropping the deck column may be necessary if it has too many missing values or is not useful for the analysis.