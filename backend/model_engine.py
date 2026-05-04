from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from backend.preprocessing import prepare_features
from backend.evaluation_engine import evaluate_model

MODELS_DIR = Path('models')
DATASET_PATH = Path('data/agri_dataset.csv')


def train_models():
    df = pd.read_csv(DATASET_PATH)
    Xs, y, scaler, label_encoder = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split(Xs, y, test_size=0.2, random_state=42, stratify=y)

    models = {
        'logistic_regression': LogisticRegression(max_iter=5000),
        'knn': KNeighborsClassifier(n_neighbors=7),
        'svm': SVC(probability=True),
        'decision_tree': DecisionTreeClassifier(random_state=42),
        'random_forest': RandomForestClassifier(n_estimators=300, random_state=42),
    }

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    metrics = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        metrics[name] = evaluate_model(y_test, y_pred)
        joblib.dump(model, MODELS_DIR / f'{name}.pkl')

    joblib.dump(scaler, MODELS_DIR / 'scaler.pkl')
    joblib.dump(label_encoder, MODELS_DIR / 'label_encoder.pkl')
    with open(MODELS_DIR / 'metrics.json', 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2)
    print('Training complete. Models and metrics saved in models/.')

if __name__ == '__main__':
    train_models()
