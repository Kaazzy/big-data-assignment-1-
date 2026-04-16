import sys
import pandas as pd
import subprocess

df = pd.read_csv(sys.argv[1])

# Insight 1 - Statistical Summary
with open("insight1.txt", "w") as f:
    f.write("=== STATISTICAL SUMMARY ===\n")
    f.write(f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n\n")
    f.write(df.describe().to_string())

# Insight 2 - Top Correlated Features
with open("insight2.txt", "w") as f:
    corr = df.corr(numeric_only=True)
    top = corr.unstack().sort_values(ascending=False)
    top = top[top < 1].drop_duplicates()
    f.write("=== TOP CORRELATED FEATURE PAIRS ===\n")
    f.write(top.head(10).to_string())

# Insight 3 - Column Types
with open("insight3.txt", "w") as f:
    f.write("=== COLUMN DATA TYPES ===\n")
    f.write(df.dtypes.to_string())
    f.write("\n\n=== NULL VALUES REMAINING ===\n")
    f.write(df.isnull().sum().to_string())

print("[analytics] 3 insights saved.")
subprocess.run(["python", "visualize.py", "data_preprocessed.csv"])