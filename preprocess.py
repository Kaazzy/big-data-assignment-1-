import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.decomposition import PCA
import subprocess

df = pd.read_csv(sys.argv[1])

# ── 1. DATA CLEANING ──────────────────────────────────────
df.drop_duplicates(inplace=True)

for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].median(), inplace=True)

for col in df.select_dtypes(include="object").columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ── 2. FEATURE TRANSFORMATION ─────────────────────────────
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col].astype(str))

scaler = MinMaxScaler()
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

col = numeric_cols[0]
Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
IQR = Q3 - Q1
df = df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]

# ── 3. DIMENSIONALITY REDUCTION ───────────────────────────
if df.shape[1] > 10:
    pca = PCA(n_components=10)
    pca_result = pca.fit_transform(df.select_dtypes(include=np.number))
    df = pd.DataFrame(pca_result, columns=[f"PC{i+1}" for i in range(10)])

# ── 4. DISCRETIZATION ─────────────────────────────────────
first_col = df.columns[0]
df[f"{first_col}_binned"] = pd.cut(
    df[first_col], bins=4,
    labels=["low", "medium", "high", "very_high"]
)
df[f"{first_col}_binned"] = df[f"{first_col}_binned"].astype(str)

df.to_csv("data_preprocessed.csv", index=False)
print(f"[preprocess] Done. Shape: {df.shape}. Saved as data_preprocessed.csv")

subprocess.run(["python", "analytics.py", "data_preprocessed.csv"])