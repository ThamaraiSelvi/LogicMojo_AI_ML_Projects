#Q3. Feature Scaling using NumPy (Very Important)

#Context: Most ML models require normalized data.

#Dataset: Iris (NumPy array)

#Tasks:
import numpy as np
import sklearn.datasets as datasets
iris = datasets.load_iris()
X = iris.data
#1. Apply standardization:

#$$
#X' = \frac{X - \mu}{\sigma}
#$$
X_mean = np.mean(X, axis=0)
print(X_mean)
X_std = np.std(X, axis=0)
print(X_std)
X_standardized = (X - X_mean) / X_std
print(X_standardized)

#​2. Verify:

#Mean ≈ 0
#Std ≈ 1
#on standardized data   