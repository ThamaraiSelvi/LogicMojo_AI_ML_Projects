#Q13. Custom Feature Transformation using apply()

#Context: Real ML requires custom logic transformation.

#Dataset: Titanic
import seaborn as sns
titanic_df = sns.load_dataset("titanic")
#Tasks:

# 1. Create age_group:
# Child / Adult / Senior
def age_group(age):
    if age < 18:
        return "Child"
    elif 18 <= age < 60:
        return "Adult"
    else:
        return "Senior"

titanic_df['age_group'] = titanic_df['age'].apply(age_group)

# 2. Use .apply()
# 3. Compute survival rate per group
survival_rate = titanic_df.groupby('age_group')['survived'].mean()
print(survival_rate)
# 4. Interpret:
# Which segment has highest survival likelihood
highest_survival_group = survival_rate.idxmax()
highest_survival_rate = survival_rate.max()
print(f"Highest survival likelihood is in the {highest_survival_group} group with a rate of {highest_survival_rate:.2f}")