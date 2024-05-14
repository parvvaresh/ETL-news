import pandas as pd
import numpy as np


class MinMaxScaler:
  def __init__(self):
    pass

  def fit(self,  df, columns):
    self.df = df
    self.columns = columns

    normalized_df = []
    for index in range(0, df.shape[0]):
      row = self.df.iloc[index]
      temp = []
      for column in self.columns:
        Max = df[column].max()
        Min = df[column].min()
        temp.append((row[column] - Min) / (Max - Min))
      normalized_df.append(temp)
    return np.array(normalized_df)