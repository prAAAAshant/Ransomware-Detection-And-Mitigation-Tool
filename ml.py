import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

# Define the dataset file path
DATASET_FILE = 'ransomware_dataset.csv'

# Define the model and scaler
model = RandomForestClassifier(n_estimators=100, random_state=42)
scaler = StandardScaler()

# Function to train the model
def train_model():
    try:
        # Load dataset
        data = pd.read_csv(DATASET_FILE)
        X = data.drop('label', axis=1)
        y = data['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
    except Exception as e:
        print(f"Error training model: {e}")