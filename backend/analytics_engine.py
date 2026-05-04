import json
from pathlib import Path
import joblib
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def compute_analytics(dataset_path: Path = Path('data/agri_dataset.csv')):
    df = pd.read_csv(dataset_path)
    X = df[['temp', 'humidity', 'rainfall', 'N', 'P', 'K']]
    pca = PCA(n_components=2, random_state=42)
    pca_points = pca.fit_transform(X)

    kmeans = KMeans(n_clusters=4, n_init=20, random_state=42)
    clusters = kmeans.fit_predict(X)

    rf = joblib.load(Path('models/random_forest.pkl'))
    importance = dict(zip(X.columns, rf.feature_importances_.tolist()))

    result = {
        'pca_explained_variance': pca.explained_variance_ratio_.tolist(),
        'pca_points': [{'x': float(a), 'y': float(b), 'state': s, 'crop': c} for (a, b), s, c in zip(pca_points, df['state'], df['crop'])],
        'clusters': [{'cluster': int(cl), 'temp': float(t), 'humidity': float(h), 'rainfall': float(r)} for cl, t, h, r in zip(clusters, df['temp'], df['humidity'], df['rainfall'])],
        'feature_importance': importance,
    }
    with open('models/analytics.json', 'w', encoding='utf-8') as f:
        json.dump(result, f)
    return result
