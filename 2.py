import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("spam.csv")

print(df.columns)

# Select required columns
df = df[['v1', 'v2']]
df = df.dropna()

# Input and output
x = df['v2']
y = df['v1']

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# Convert text into numbers
tfidf = TfidfVectorizer()
x_train = tfidf.fit_transform(x_train)
x_test = tfidf.transform(x_test)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
p1 = knn.predict(x_test)

# SVM
svm = SVC(kernel='linear')
svm.fit(x_train, y_train)
p2 = svm.predict(x_test)

# Evaluation
print("KNN Accuracy:", accuracy_score(y_test, p1))
print("SVM Accuracy:", accuracy_score(y_test, p2))