from typing import Dict, Tuple

STATE_BOUNDING_BOXES: Dict[str, Tuple[float, float, float, float]] = {
    "Jammu & Kashmir": (32.0, 37.5, 73.0, 80.5), "Himachal Pradesh": (30.4, 33.3, 75.5, 79.0),
    "Punjab": (29.5, 32.6, 73.8, 76.9), "Haryana": (27.6, 30.9, 74.4, 77.6), "Delhi": (28.4, 28.9, 76.8, 77.4),
    "Uttarakhand": (28.4, 31.5, 77.5, 81.2), "Rajasthan": (23.0, 30.0, 69.5, 78.5), "Gujarat": (20.1, 24.8, 68.0, 74.5),
    "Maharashtra": (15.6, 22.1, 72.6, 80.9), "Goa": (14.9, 15.8, 73.6, 74.3), "Madhya Pradesh": (21.0, 26.9, 74.0, 82.8),
    "Chhattisgarh": (17.8, 24.1, 80.2, 84.4), "Bihar": (24.0, 27.5, 83.3, 88.2), "Jharkhand": (21.9, 25.3, 83.3, 87.9),
    "West Bengal": (21.4, 27.2, 85.8, 89.9), "Odisha": (17.8, 22.7, 81.2, 87.5), "Telangana": (15.8, 19.9, 77.1, 81.0),
    "Andhra Pradesh": (12.6, 19.9, 76.8, 84.8), "Karnataka": (11.5, 18.5, 74.0, 78.7), "Kerala": (8.1, 12.8, 74.8, 77.6),
    "Tamil Nadu": (8.0, 13.6, 76.0, 80.4), "Assam": (24.0, 28.0, 89.7, 96.1), "Meghalaya": (25.0, 26.1, 89.8, 92.8),
    "Tripura": (22.9, 24.5, 91.0, 92.4), "Manipur": (23.8, 25.7, 93.0, 94.8), "Nagaland": (25.1, 27.1, 93.2, 95.3),
    "Mizoram": (21.9, 24.5, 92.2, 93.5), "Arunachal Pradesh": (26.6, 29.5, 91.2, 97.5), "Sikkim": (27.0, 28.2, 88.0, 88.9),
}


def map_lat_lon_to_state(lat: float, lon: float) -> str:
    for state, (min_lat, max_lat, min_lon, max_lon) in STATE_BOUNDING_BOXES.items():
        if min_lat <= lat <= max_lat and min_lon <= lon <= max_lon:
            return state
    return "Madhya Pradesh"
