import pandas as pd
import numpy as np



class cosine_similary:
  def __init__(self):
    pass  
    
  def Internal_multiplication(self, vector_1, vector_2):
    sum = 0
    if len(vector_1) != len(vector_2):
      return False
    else:
      for index in range(0, len(vector_1)):
        sum += (vector_1[index]) * (vector_2[index])
    return sum

  def Measure_the_vector(self, vector):
    from math import sqrt
    sum_power = 0
    for element in vector:
      sum_power += element ** 2
    return sqrt(sum_power)

  def calcute(self, vector_1, vector_2):
    return (self.Internal_multiplication(vector_1, vector_2)) / (self.Measure_the_vector(vector_1) * self.Measure_the_vector(vector_2))

  def fit(self, df):
    self.df = df
    cosine_similary = []
    for vector in self.df:
      temp = []
      for vector_test in self.df:
        temp.append(self.calcute(list(vector), list(vector_test)))
      cosine_similary.append(temp)
    return np.array(cosine_similary)