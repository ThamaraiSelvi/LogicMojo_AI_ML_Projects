#Q7. Feature Engineering for Model Improvement

#Context: Raw data is rarely useful—features must be created.

#Dataset: Titanic
import seaborn as sns
titanic_df = sns.load_dataset("titanic")
#Tasks:

#1. Create:
#family_size = sibsp + parch + 1
#2. Create:
#is_alone (binary feature)
#3. Compute survival rate by is_alone

#1. Create:
titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch'] + 1
print(titanic_df['family_size'])
#2. Create:
titanic_df['is_alone'] = (titanic_df['family_size'] == 1).astype(int)
print(titanic_df['is_alone'])
#3. Compute survival rate by is_alone
survival_rate = titanic_df.groupby('is_alone')['survived'].mean()
print(survival_rate)
#4. Explain:
#Engineered features improve ML models by providing more relevant information, capturing complex patterns, and enhancing model performance.