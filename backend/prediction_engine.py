from pathlib import Path
import random
import joblib
from backend.state_data import state_data
from backend.data_engine import generate_sample

MODELS = {}


def load_artifacts():
    for name in ['logistic_regression', 'knn', 'svm', 'decision_tree', 'random_forest']:
        MODELS[name] = joblib.load(Path('models') / f'{name}.pkl')
    MODELS['scaler'] = joblib.load(Path('models/scaler.pkl'))
    MODELS['label_encoder'] = joblib.load(Path('models/label_encoder.pkl'))


def _clip(value, lo, hi):
    return max(lo, min(hi, value))


def predict(state: str, payload: dict):
    if not MODELS:
        load_artifacts()
    cfg = state_data[state]
    sample = generate_sample(state)
    for key, rng in [('temp', cfg['temp']), ('humidity', cfg['humidity']), ('rainfall', cfg['rainfall'])]:
        if payload.get(key) is not None:
            sample[key] = _clip(float(payload[key]), rng[0], rng[1])
    for key in ['N', 'P', 'K']:
        if payload.get(key) is not None:
            r = cfg['npk'][key]
            sample[key] = _clip(float(payload[key]), r[0], r[1])

    model_name = payload.get('model', 'random_forest')
    model = MODELS.get(model_name, MODELS['random_forest'])
    X = [[sample['temp'], sample['humidity'], sample['rainfall'], sample['N'], sample['P'], sample['K']]]
    Xs = MODELS['scaler'].transform(X)
    pred_idx = model.predict(Xs)[0]
    crop = MODELS['label_encoder'].inverse_transform([pred_idx])[0]
    probs = model.predict_proba(Xs)[0] if hasattr(model, 'predict_proba') else None
    conf = float(max(probs)) if probs is not None else 0.75

    disease = 'High' if sample['humidity'] > 85 else 'Medium' if sample['humidity'] > 65 else 'Low'
    rain_mid = sum(cfg['rainfall']) / 2
    yield_pred = 'High' if abs(sample['rainfall'] - rain_mid) < 0.2 * rain_mid else 'Medium' if abs(sample['rainfall'] - rain_mid) < 0.4 * rain_mid else 'Low'
    return {
        'state': state, 'crop_prediction': crop, 'yield_prediction': yield_pred,
        'disease_risk': disease, 'confidence': round(conf, 4), 'input_features': sample
    }
