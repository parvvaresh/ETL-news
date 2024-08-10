from sklearn.neighbors import KNeighborsClassifier

def get_knn():
    param_knn = {
        'n_neighbors': list(range(1, 15, 2)),
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan', 'minkowski']
    }
    return KNeighborsClassifier() , param_knn