import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load data
customer_data = pd.read_csv('customer_churn_data.csv')

# Feature engineering
X = customer_data[['age', 'gender', 'income', 'tenure', 'monthly_usage_gb', 'monthly_calls']]
X = pd.get_dummies(X, columns=['gender'], drop_first=True)  # One-hot encoding for gender
y = customer_data['churn']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Evaluate model performance
print(classification_report(y_test, y_pred))
