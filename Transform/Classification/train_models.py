import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from parameter_finder import classification_parameter_finder
from models.models import get_details_models

import warnings
from sklearn.exceptions import ConvergenceWarning

# Ignore ConvergenceWarning
warnings.filterwarnings("ignore", category = ConvergenceWarning)


def train_models(X : np.array,
                 y : pd.DataFrame):
    

    results = []


    print("📌start train model ...")

    details_models = get_details_models()
    for detail_model in details_models:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model, parameters = detail_model

        print(f"--- 📌start train <<{model}>> on data")

        _result = classification_parameter_finder(model,
                                                parameters,
                                                X_train,
                                                y_train,
                                                X_test,
                                                y_test)
                
        print(f"--- ✅finish train <<{model}>> on data")

        results.append(_result)
        results_df = pd.concat(results, ignore_index=True)
        results_df.to_csv("./result/result.csv")



    print("✅finish train model")

    results = pd.concat(results, ignore_index=True)

    results.to_csv("./result/result.csv")

    print("             ✅save result in local path✅              ")