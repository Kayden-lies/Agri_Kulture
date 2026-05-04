import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def prepare_features(df: pd.DataFrame):
    crop_encoder = LabelEncoder()
    df = df.copy()
    df['crop_encoded'] = crop_encoder.fit_transform(df['crop'])
    X = df[['temp', 'humidity', 'rainfall', 'N', 'P', 'K']]
    y = df['crop_encoded']
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    return Xs, y, scaler, crop_encoder
