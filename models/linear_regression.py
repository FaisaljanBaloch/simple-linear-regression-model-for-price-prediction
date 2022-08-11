import numpy as np
import pandas as pd

class LinearRegression():
    """LinearRegression model predicts the house price based on the house square feet of living."""

    def __init__(self):
        # reading data from CSV files
        dataset = pd.read_csv('kc_house_data.csv')
        dataset = dataset.head(2000) # Split only first 1000 rows

        # seprating the xAxis and yAxis
        self.y = np.array(dataset.price).reshape(len(dataset.price), 1)
        self.x = np.transpose([np.ones(len(self.y)), dataset.sqft_living])
        self.theta = np.array([[0.3], [0.5]])
        self.m = len(self.y)


    def predict(self, sqft_living):
        """
        Returns the price of the house by given size in square feet.

        Parameter:
            sqft_living (int): Size of the house
        Returns:
            price (int): Price of the house based on given size. 
        """
        params = self.__gradient_descent(0.00000001, 3500)

        # we need to make a vector [[1], [1]]
        x2 = np.array([[1], [sqft_living]])
        x2 = np.transpose(x2)
        y2 = self.__hypothises(x2, params)
        predicted_price = np.abs(np.round(y2[0][0], 2))
        
        return predicted_price

    def __cost_function(self):
        h = self.__hypothises(self.x, self.theta)
        hy = h - self.y
        hy = np.square(hy)
        cost = 1/(2*self.m) * np.sum(hy)
        return cost


    def __hypothises(self, xAxis, yAxis):
        return np.dot(xAxis, yAxis)


    def __gradient_descent(self, alpha, iteration):
        iter = 0
        while iter < iteration:
            h = self.__hypothises(self.x, self.theta)
            hy = h - self.y
            self.theta[0][0] = self.theta[0][0] - alpha/self.m * sum(hy)
            self.theta[1][0] = self.theta[1][0] - alpha/self.m * np.sum(np.dot(np.transpose(hy), self.x[:,  1]))
            cost = self.__cost_function()
            # print(theta[0][0], theta[1][0], cost)
            iter += 1

        return self.theta