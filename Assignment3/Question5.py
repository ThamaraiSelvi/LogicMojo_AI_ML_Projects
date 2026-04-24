#Q5. Filtering Data for Business Logic

#Context: Real ML problems require filtering relevant populations.

#Dataset: Titanic

#Tasks:
import seaborn as sns
titanic_df = sns.load_dataset("titanic")

#1. Filter:
female_passengers = titanic_df[(titanic_df['sex'] == 'female') & (titanic_df['pclass'] == 1)]
print(female_passengers)
#2. Compute:
survival_rate = female_passengers['survived'].mean()
print(survival_rate)
#3. Compare with overall survival rate
overall_survival_rate = titanic_df['survived'].mean()
print(overall_survival_rate)
#4. Interpret:
#The survival rate of female passengers in 1st class is higher than the overall rate, indicating that class and gender are important features for predicting survival.