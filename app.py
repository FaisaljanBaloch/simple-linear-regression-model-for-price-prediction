import numpy as np
import pandas as pd
from gradient_descent import gradient_descent
from hypothises import hypothises

# MY datas for the model
data = pd.read_csv('kc_house_data.csv')
newData = data.head(1000)
y = newData.price
x = newData.sqft_living

y = np.array(y).reshape(len(y), 1)

x = np.transpose([np.ones(len(y)), x])
theta = np.array([[0.3], [0.5]])
params = gradient_descent(x, y, theta, 0.00000001, 3500)

x2 = [2500, 2950]
x2 = np.transpose(np.array(x2))
x2 = np.transpose([np.ones(len(x2)), x2])
y2 = hypothises(x2, params)

for i in range(len(x2)):
    print(f"Size {x2[i]} : Prize {y2[i]} ")