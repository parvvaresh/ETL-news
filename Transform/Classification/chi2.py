import numpy as np
from sklearn.feature_selection import SelectKBest, chi2



def select_best_feature(X_train : np.array, y_train : np.array, X_test : np.array, k=200) -> list:



    transformer = SelectKBest(chi2, k = k).fit(X_train, y_train)
    X_train_transform = transformer.transform(X_train)
    X_test_transform = transformer.transform(X_test)

    return X_train_transform, X_test_transform