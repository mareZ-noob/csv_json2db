import os, shutil, codecs, json, psycopg2
import pandas as pd
import csv

df = pd.read_json("data.json")
print(df.head())
df.fillna(0)
df.to_csv(path_or_buf="json2csv.csv", encoding="utf-8", index=False)


