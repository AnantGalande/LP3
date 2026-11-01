import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin-1')

print(df.columns)

# Preprocessing
df = df.dropna()

# Select required columns
x = df[['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'MSRP']]

# Feature scaling
sc = StandardScaler()
x = sc.fit_transform(x)

# Elbow Method
wcss = []

for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42, n_init=10)
    km.fit(x)
    wcss.append(km.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# K-Means Clustering
km = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = km.fit_predict(x)

# Display result
print(df[['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'Cluster']].head())

print("Clustering completed")