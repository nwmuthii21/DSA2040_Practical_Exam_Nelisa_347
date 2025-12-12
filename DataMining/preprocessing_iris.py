import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# 1. LOAD DATASET
iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
)
df["species"] = iris.target

print("\n✅ Dataset Loaded Successfully")
print(df.head())

# 2. PREPROCESSING

# Check for missing values
print("\n✅ Missing Value Check:")
print(df.isnull().sum())

df.fillna(df.mean(), inplace=True)

# Normalize features using Min-Max scaling
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(df.iloc[:, :4])
df_scaled = pd.DataFrame(scaled_features, columns=df.columns[:4])
df_scaled["species"] = df["species"]

print("\n✅ Normalization Complete")
print(df_scaled.head())

# Encode class label (One-Hot)
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df[["species"]])
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(["species"]))

df_encoded = pd.concat([df_scaled.iloc[:, :4], encoded_df], axis=1)

print("\n✅ Encoding Complete")
print(df_encoded.head())

# 3. EXPLORATION & VISUALIZATION
# Summary statistics
print("\n✅ Summary Statistics:")
print(df.describe())

# Pairplot
sns.pairplot(df, hue="species")
plt.savefig("pairplot_iris.png")
plt.close()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.iloc[:, :4].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.close()

# Boxplots for outlier detection
plt.figure(figsize=(10, 6))
df.iloc[:, :4].boxplot()
plt.title("Boxplots for Outlier Detection")
plt.savefig("boxplots_outliers.png")
plt.close()

print("\n✅ Visualizations Saved: pairplot_iris.png, correlation_heatmap.png, boxplots_outliers.png")

# 4. TRAIN/TEST SPLIT FUNCTION
def split_data(df, test_size=0.2):
    X = df.iloc[:, :4]
    y = df["species"]
    return train_test_split(X, y, test_size=test_size, random_state=42)

X_train, X_test, y_train, y_test = split_data(df)

print("\n✅ Train/Test Split Complete")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
