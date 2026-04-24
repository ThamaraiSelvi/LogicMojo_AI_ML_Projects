#Q15. Business + ML Insight Problem (Tips Dataset)

#Context: Convert data analysis into decision-making

import seaborn as sns
tips_df = sns.load_dataset("tips")

#Tasks:

#1. Create:
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100

#2. Group by:
grouped = tips_df.groupby(['day', 'time']).agg({'tip_percentage': 'mean'}).reset_index()
print(grouped)

#3. Identify:
highest_revenue_segment = grouped.loc[grouped['tip_percentage'].idxmax()]
print(f"Highest revenue segment: {highest_revenue_segment['day']} during {highest_revenue_segment['time']} with an average tip percentage of {highest_revenue_segment['tip_percentage']:.2f}%")

#4. Provide:
#recommendation = f"Focus on {highest_revenue_segment['day']} during {highest_revenue_segment['time']} for maximizing tips."
#how_ml_can_help = "ML models can analyze past tipping patterns to predict future trends and optimize staff allocation."
