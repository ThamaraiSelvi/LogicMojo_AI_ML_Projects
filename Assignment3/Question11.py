#Q11. End-to-End ML Preprocessing Pipeline (Titanic)

#Context: Prepare dataset for ML model training

#Tasks:

#1. Load dataset
from turtle import pd
import seaborn as sns
titanic_df = sns.load_dataset("titanic")
#2. Handle missing values
titanic_df = titanic_df.dropna()    
print(titanic_df.isnull().sum())
#3. Encode categorical variables (sex, embarked)
print(pd.get_dummies(titanic_df, columns=["sex", "embarked"], drop_first=True))

#4. Normalize numerical features 
#5. Convert to NumPy array
final_features = titanic_df.values

#Output:

#Final feature matrix ready for model training