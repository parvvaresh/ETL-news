import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    recall_score,
    accuracy_score,
    precision_score,
    f1_score,
    confusion_matrix,
    cohen_kappa_score,
    make_scorer
)

import numpy as np
import pandas as pd
import time

import warnings
warnings.filterwarnings("ignore")






def classification_parameter_finder(model,
                                    parameters : dict,
                                    X_train : np.array,
                                    y_train : np.array,
                                    X_test : np.array,
                                    y_test : np.array) -> pd.DataFrame:
    start = time.time()

    kappa_scorer = make_scorer(cohen_kappa_score)

    grid = GridSearchCV(model,
                        param_grid=parameters,
                        refit=True,
                        cv=5, 
                        n_jobs=-1,
                        scoring=kappa_scorer)
    grid.fit(X_train, y_train)

    y_train_pred = grid.predict(X_train)
    y_test_pred = grid.predict(X_test)

    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)

    precision = precision_score(y_test, y_test_pred, average='weighted')
    recall = recall_score(y_test, y_test_pred, average='weighted')
    f1 = f1_score(y_test, y_test_pred, average='weighted')
    kappa = cohen_kappa_score(y_test, y_test_pred)

    conf_matrix = confusion_matrix(y_test, y_test_pred)
    class_labels = np.unique(y_test)

    model_name = str(model).split('(')[0]

    end = time.time()

    results = pd.DataFrame({
        "model": [model_name],
        "best_params": [grid.best_params_],
        "train_accuracy": [train_accuracy],
        "test_accuracy": [test_accuracy],
        "precision": [precision],
        "recall": [recall],
        "f1_score": [f1],
        "kappa": [kappa],
        "confusion_matrix": [conf_matrix.ravel()],
        "runtime": [end - start],
        "best model" : [grid.best_estimator_]
    })

    return results