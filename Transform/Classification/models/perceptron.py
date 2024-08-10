from sklearn.linear_model import Perceptron

def get_pr():

    param_perceptron = {
        'penalty': ['l1', 'l2', 'elasticnet'],
        'alpha': [0.0001, 0.001, 0.01, 0.1, 1],
        'max_iter': [1000, 2000, 3000]
    }

    return Perceptron() , param_perceptron