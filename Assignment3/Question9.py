#Q9. Advanced Filtering + Subsetting

#Context: Training data is often filtered based on business rules.

#Dataset: Tips 
import seaborn as sns

tips_df = sns.load_dataset("tips")

#Tasks:

#1. Filter:
#total_bill > 20 AND tip < 3
filtered_tips = tips_df[(tips_df['total_bill'] > 20) & (tips_df['tip'] < 3)]
print(filtered_tips)
#2. Select only relevant columns
relevant_columns = filtered_tips[['total_bill', 'tip']]
print(relevant_columns)
#3. Analyze:
#Is this segment under-tipping?
average_tip = relevant_columns['tip'].mean()
print(average_tip)
##4. Explain:
#How such filtering helps anomaly detection