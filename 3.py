import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Churn_Modelling.csv")

print(df.columns)

# Preprocessing
df = df.dropna()

df = df[['CreditScore', 'Geography', 'Gender', 'Age',
         'Tenure', 'Balance', 'NumOfProducts',
         'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited']]

# Input and output
x = df[['CreditScore', 'Geography', 'Gender', 'Age',
        'Tenure', 'Balance', 'NumOfProducts',
        'HasCrCard', 'IsActiveMember', 'EstimatedSalary']]

y = df['Exited']

# Convert categorical data into numbers
x = pd.get_dummies(x, columns=['Geography', 'Gender'], drop_first=True)

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Neural Network
model = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=300, random_state=42)

model.fit(x_train, y_train)
p = model.predict(x_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, p))