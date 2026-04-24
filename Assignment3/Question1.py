#Q1. Understanding Feature Distributions (Iris Dataset)

#Context: Before training any ML model, we analyze feature distributions.

#Dataset: Load Iris dataset from sklearn 
import numpy as np
import sklearn.datasets as datasets
iris = datasets.load_iris()


#Tasks:

#1. Extract feature matrix as NumPy array
X = iris.data

#2. Compute:
#Mean
print(np.mean(X, axis=0))

#Median
print(np.median(X, axis=0))

#Standard deviation
print(np.std(X, axis=0))
#Variance (for each feature)
var = np.var(X, axis=0)
print(var)

#3. Identify:
#Which feature has highest variability and why it matters in ML
highest_variability_feature = np.argmax(var)
highest_variability_value = var[highest_variability_feature]
# It matters because features with higher variability can provide more information to the model.

#4. Convert any one feature into shape (n,1) and explain why ML models expect this format
X_reshaped = X[:, highest_variability_feature].reshape(-1, 1)
print(X_reshaped)
# ML models expect this format because they require a 2D array for input, where each column represents a feature.
