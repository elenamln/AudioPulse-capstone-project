import pandas as pd
import glob
import json

json_files = glob.glob("audio_output/*.json")

df = pd.DataFrame()

for file in json_files:
	with open(file, "r", encoding="utf-8") as f:
		data = json.load(f)
		records = data if isinstance(data, list) else [data]
		df = pd.concat([df, pd.DataFrame(records)], ignore_index=True)

print(df.head())

df.to_csv("combined_metadata.csv", index=False)