from backend.model_engine import train_models
from backend.analytics_engine import compute_analytics
if __name__ == '__main__':
    train_models()
    compute_analytics()
    print('Analytics generated: models/analytics.json')
