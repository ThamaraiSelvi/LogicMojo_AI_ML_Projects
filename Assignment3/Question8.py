#Q8. Group-Based Insights (Customer Segmentation Logic)

#Context: ML models often depend on aggregated patterns.

#Dataset: Tips
import seaborn as sns
tips_df = sns.load_dataset("tips")

#Tasks:

#1. Compute:
#Average tip by day
average_tip = tips_df.groupby('day')['tip'].mean()
print(average_tip)
#Total bill by gender
total_bill = tips_df.groupby('sex')['total_bill'].sum()
print(total_bill)
#2. Create new feature:
#tip_percentage
tips_df['tip_percentage'] = (tips_df['tip'] / tips_df['total_bill']) * 100
print(tips_df['tip_percentage'])
#3. Identify:
#Which day has highest tipping behavior
highest_tipping_day = tips_df.groupby('day')['tip'].mean().idxmax()
print(highest_tipping_day)
#4. Explain:
#How this helps in segmentation models
#Understanding tipping behavior by day and gender allows for targeted marketing strategies, such as promotions on high-tipping days or tailored offers for different customer segments.
