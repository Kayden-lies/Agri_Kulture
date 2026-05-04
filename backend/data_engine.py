import random
from backend.state_data import state_data

def _level(x, lo, hi):
    r = (x - lo) / max(1e-6, (hi - lo))
    return min(max(r, 0), 1)

def generate_sample(state: str):
    s = state_data[state]
    temp = random.uniform(*s['temp'])
    humidity = random.uniform(*s['humidity'])
    rainfall = random.uniform(*s['rainfall'])
    n = random.uniform(*s['npk']['N'])
    p = random.uniform(*s['npk']['P'])
    k = random.uniform(*s['npk']['K'])
    crop = random.choice(s['crops'])

    rain_score = _level(rainfall, *s['rainfall'])
    hum_score = _level(humidity, *s['humidity'])
    yield_score = 0.6 * rain_score + 0.4 * (1 - abs(hum_score - 0.55))
    yield_label = 'High' if yield_score >= 0.67 else 'Medium' if yield_score >= 0.4 else 'Low'

    if humidity > 85:
        disease = 'High'
    elif humidity > 65:
        disease = 'Medium'
    else:
        disease = 'Low'

    return {
        'state': state, 'temp': round(temp, 2), 'humidity': round(humidity, 2), 'rainfall': round(rainfall, 2),
        'N': round(n, 2), 'P': round(p, 2), 'K': round(k, 2), 'crop': crop, 'yield': yield_label, 'disease': disease
    }
