from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class TimeSeriesScaler(TransformerMixin, BaseEstimator):
    """
    A TimeSeriesScaler to scale 3D numpy arrays for LSTM, where the array is sample x timesteps x features.
    """

    def __init__(self, scaler_type: str = 'standard'):
        self.scaler_type = scaler_type

    def fit(self, X, y=None):
        # Fit on the flattened numpy array
        if self.scaler_type == 'standard':
            self.scaler_ = StandardScaler().fit(self.flatten(X))

        elif self.scaler_type == 'robust':
            self.scaler_ = RobustScaler().fit(self.flatten(X))

        elif self.scaler_type == 'min-max':
            self.scaler_ = MinMaxScaler().fit(self.flatten(X))

        return self

    def transform(self, X):
        X = self.scale(X)

        return X

    def flatten(self, X):
        """
        Flatten a 3D array.
        :param X: A 3D numpy array for LSTM, where the array is sample x timesteps x features.
        :return: A 2D array, sample x features.
        """

        flattened_X = np.empty((X.shape[0], X.shape[2]))  # sample x features array.
        for i in range(X.shape[0]):
            flattened_X[i] = X[i, (X.shape[1] - 1), :]

        return flattened_X

    def scale(self, X):
        """
        Scale 3D array.
        :param X: A 3D array for LSTM, where the array is sample x timesteps x features.
        :return: Scaled 3D array for lstm, where the array is sample x timesteps x features.
        """
        scaled_array = np.array([])
        for i in range(X.shape[0]):
            scaled_array = np.append(scaled_array, self.scaler_.transform(X[i, :, :]))

        return scaled_array.reshape(X.shape)
