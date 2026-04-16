import sys
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv(sys.argv[1])
numeric_df = df.select_dtypes(include="number").dropna()
features = numeric_df.iloc[:, :5]

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(features)

counts = pd.Series(labels).value_counts().sort_index()

with open("clusters.txt", "w") as f:
    f.write("=== K-MEANS CLUSTERING RESULTS (k=4) ===\n\n")
    for cluster_id, count in counts.items():
        f.write(f"Cluster {cluster_id}: {count} samples\n")

print("[cluster] clusters.txt saved.")