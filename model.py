from sklearn.linear_model import LinearRegression

import numpy as np

def train():
    # Generate some example data
    x = np.array([[1], [2], [3], [4],[5]])
    y = np.array([5,7,9,11,13])

    # Create a linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(x, y)

    return model
    

