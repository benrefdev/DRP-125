import pandas as pd

#Membentuk data frame
df = pd.read_csv("music_genre.csv", sep=",")
print(df.shape)
print(df.head(),"\n")

#Terdapat 50k baris dengan 18 kolom
print(df.info())

#Cek data kosong
print(f"\njumlah data kosong pada masing-masing kolom:\n{df.isna().sum()}")

#Cek duplikat
print("\njumlah data duplikat:", df.duplicated().sum())

#Pembersihan data
df["artist_name"] = df["artist_name"].str.strip()
df["track_name"] = df["track_name"].str.strip()
df["key"] = df["key"].str.strip()
df["mode"] = df["mode"].str.strip()
df["tempo"] = df["tempo"].str.strip()
df["obtained_date"] = df["obtained_date"].str.strip()
df["music_genre"] = df["music_genre"].str.strip()

df = df.drop_duplicates()
df = df.dropna()

#Hasil data setelah pembersihan
print("\nHasil data frame bersih:")
print(df.shape)
print(df.describe(),"\n")
print(df.head())