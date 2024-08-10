from sklearn.ensemble import RandomForestClassifier

def get_rf():
        
    param_randomForest = {
        'n_estimators': [50, 100, 200],
        'criterion': ['gini', 'entropy'],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    return RandomForestClassifier() , param_randomForest