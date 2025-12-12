import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD & PREPROCESS 
iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
)
df["species"] = iris.target
# Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df.iloc[:, :4])

# 2. K-MEANS CLUSTERING (k = 3)
kmeans_3 = KMeans(n_clusters=3, random_state=42)
clusters_3 = kmeans_3.fit_predict(X_scaled)
# Compare with actual classes using Adjusted Rand Index
ari_3 = adjusted_rand_score(df["species"], clusters_3)
print(f"\n✅ ARI for k=3: {ari_3:.4f}")

# 3. EXPERIMENT: k = 2 and k = 4
k_values = [2, 3, 4]
ari_scores = []

for k in k_values:
    km = KMeans(n_clusters=k, random_state=42)
    preds = km.fit_predict(X_scaled)
    ari_scores.append(adjusted_rand_score(df["species"], preds))

print("\n✅ ARI Scores for k=2,3,4:", ari_scores)

# 4. ELBOW CURVE
inertia_values = []
K_range = range(1, 10)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia_values.append(km.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia_values, marker="o")
plt.title("Elbow Curve for Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()

# 5. CLUSTER VISUALIZATION
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x=df["petal_length"],
    y=df["petal_width"],
    hue=clusters_3,
    palette="viridis"
)
plt.title("K-Means Clusters (k=3) – Petal Length vs Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.tight_layout()
plt.savefig("cluster_scatter.png")
plt.close()

print("\n✅ Visualizations Saved: elbow_curve.png, cluster_scatter.png")
