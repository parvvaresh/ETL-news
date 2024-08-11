import pandas as pd
import numpy as np
import sys
import os



from pre_process import preprocessing_pipline
from Classification.train_models import train_models
from Classification.word2vec import TfIdf


def process_run():
    df = pd.read_csv(r"Classification/train_data/news.csv")
    df = preprocessing_pipline(df , "title")


    print(f"--- 📌start vectorizing Tf-Idf")
    tfidf_model = TfIdf(df["Text - preproces"].to_list()) 
    tfidf_vector = tfidf_model.transform() # is X
    print(f"--- ✅finish vectorizing Tf-Idf")

    y = df["label"].to_list() # is y

    train_models(tfidf_vector, y)
    #save results
    



process_run()