from sklearn.neighbors import NearestCentroid
def get_nc():

    param_NearestCentroid =  {
        'metric': ['euclidean', 'manhattan'],
        'shrink_threshold': [None, 0.1, 0.2, 0.5, 0.7, 0.8]
        }


    return NearestCentroid(), param_NearestCentroid