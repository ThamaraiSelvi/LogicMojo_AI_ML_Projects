#Q12. Feature Selection using Statistical Understanding

#Context: Not all features improve model performance.

#Dataset: Iris
import sklearn.datasets as datasets
import pandas as pd
#Tasks:

iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

#Tasks:

#1. Compute correlation matrix
correlation_matrix = iris_df.corr()
print(correlation_matrix)

#
# 2. Identify highly correlated features
highly_correlated_features = correlation_matrix[correlation_matrix > 0.8].index.tolist()
print("Highly correlated features:", highly_correlated_features)

#3. Drop redundant features
iris_df = iris_df.drop(columns=highly_correlated_features)
print("Reduced feature set:", iris_df.columns.tolist())

# 4. Explain:
# Impact on overfitting and model performance

#Dropping highly correlated features helps in reducing overfitting by simplifying the model. It also improves model performance by eliminating redundant information, allowing the model to generalize better on unseen data.