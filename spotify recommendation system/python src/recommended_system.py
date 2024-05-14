from model.minmax_scaler import MinMaxScaler
from model.cosine_similary import cosine_similary
import pandas as pd
import numpy as np

class recommended_system:
	def __init__(self, df):
		self.normalize = MinMaxScaler()
		self.cs_model = cosine_similary()
		self.df = df
		self.columns = (df.columns)[1 : -3]
		self.fit()
		self.indices = pd.Series(self.df.index, index = df.song_title).drop_duplicates()

	def fit(self):
		self.normalized_df = self.normalize.fit(self.df, self.columns)
		self.cos_sim = self.cs_model.fit(self.normalized_df)   

	def get_name(self, title_music):
	  #get list of songs for given songs

	  similarity_song = list(enumerate(self.cos_sim[self.indices[title_music]]))

	  sorted_list = sorted(similarity_song, key = lambda x : x[1], reverse = True)
	  top_songs = sorted_list[1 : 11]
	  top_songs_index = [i[0] for i in top_songs]

	  get_name = self.df["song_title"].iloc[top_songs_index]
	  return get_name
