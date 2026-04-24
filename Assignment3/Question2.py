#Q2. Data Selection for Model Input

#Context: Models are trained on selective features, not full raw data.

#Dataset: Iris
import numpy as np
import sklearn.datasets as datasets

iris = datasets.load_iris()
X = iris.data
    
#Tasks:

#1. Extract:
#First 100 samples
X_subset = X[:100]
print(X_subset)
#Only last 2 features
X_subset = X_subset[:, -2:]
print(X_subset)
#2. Use boolean masking:
#Select samples where petal length is greater than dataset mean
mask = X[:, 2] > np.mean(X[:, 2])
selected_samples = X[mask]
print(selected_samples)
#3. Count selected samples
count = selected_samples.shape[0]
print(count)
#4. Explain how this relates to feature-based filtering in ML