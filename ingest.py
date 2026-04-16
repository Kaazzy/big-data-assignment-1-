import sys
import pandas as pd
import subprocess

filepath = sys.argv[1]
df = pd.read_csv(filepath)
df.to_csv("data_raw.csv", index=False)
print(f"[ingest] Loaded {len(df)} rows. Saved as data_raw.csv")

subprocess.run(["python", "preprocess.py", "data_raw.csv"])