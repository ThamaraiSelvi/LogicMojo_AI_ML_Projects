#Q14. Error Analysis Simulation (Model Evaluation Thinking)

#Context: Understanding prediction errors is key in ML.

#Tasks:
import numpy as np
#1. Generate 1000 random error values using NumPy
random_errors = np.random.normal(loc=0, scale=1, size=1000)
#2. Compute:
#Mean
#Standard deviation
mean_error = np.mean(random_errors)
std_error = np.std(random_errors)

#3. Identify outliers:
#Using mean ± 2*std
outliers = random_errors[(random_errors < mean_error - 2 * std_error) | (random_errors > mean_error + 2 * std_error)]
##4. Explain:
#High variance in model performance indicates that the model's predictions are highly sensitive to fluctuations in the training data. This can lead to overfitting, where the model captures noise instead of the underlying pattern.