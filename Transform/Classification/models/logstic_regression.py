from sklearn.linear_model import LogisticRegression
def get_lr():

    param_logsticRegression = {
        'penalty': ['l1', 'l2'],
        'C': [0.01, 0.1, 1, 10, 100],
        'solver': ['liblinear', 'saga'],
        'max_iter': [100, 200, 300, 500]
    }

    return LogisticRegression() , param_logsticRegression

