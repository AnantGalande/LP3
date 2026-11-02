import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv("emails.csv")

print(df.head())

# Select input features directly by column names
X = df[['the', 'to', 'ect', 'and', 'for',
        'of', 'a', 'you', 'hou', 'in',
        'on', 'is', 'this', 'i', 'it']]

# Output
y = df['the_class']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
p1 = knn.predict(X_test)

# SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
p2 = svm.predict(X_test)

# Evaluation
print("KNN Accuracy:", accuracy_score(y_test, p1))
print("SVM Accuracy:", accuracy_score(y_test, p2))

print("KNN Confusion Matrix:")
print(confusion_matrix(y_test, p1))

print("SVM Confusion Matrix:")
print(confusion_matrix(y_test, p2))