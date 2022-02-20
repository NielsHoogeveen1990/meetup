import pandas as pd
import numpy as np
from typing import List


def transform_time_series_data(df: pd.DataFrame, columns: List[str], look_back_periods: int) -> pd.DataFrame:

    X = df[columns].values
    n_features = X.shape[1]

    output_X = []
    for i in range(len(X) - look_back_periods - 1):
        t = []
        for j in range(1, look_back_periods + 1):
            # Gather the past records up to the look back period
            t.append(X[[(i + j + 1)], :])
        output_X.append(t)
    output_X = np.squeeze(np.array(output_X))

    return output_X.reshape(output_X.shape[0], look_back_periods, n_features)
