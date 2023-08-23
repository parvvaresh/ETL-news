from recommended_system import recommended_system
import pandas as pd

def main(flag = None):
	df = pd.read_csv("data.csv")
	rs = recommended_system(df)
	title_song = input("please entername of song : ")
	rs_songs = rs.get_name(title_song)
	for index, song in enumerate(rs_songs):
		print(f" {index + 1} --- > {song}")

main()