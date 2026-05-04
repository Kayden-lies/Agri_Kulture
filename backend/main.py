from pathlib import Path
import json
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from backend.state_mapper import map_lat_lon_to_state
from backend.prediction_engine import predict
from backend.analytics_engine import compute_analytics

app = FastAPI(title="Agri ML Dashboard")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")


class PredictRequest(BaseModel):
    lat: float
    lon: float
    temp: float | None = None
    humidity: float | None = None
    rainfall: float | None = None
    N: float | None = None
    P: float | None = None
    K: float | None = None
    model: str = "random_forest"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/graphs", response_class=HTMLResponse)
def graphs(request: Request):
    return templates.TemplateResponse("graphs.html", {"request": request})


@app.post("/predict")
def predict_route(req: PredictRequest):
    state = map_lat_lon_to_state(req.lat, req.lon)
    return predict(state, req.model_dump())


@app.get("/metrics")
def metrics():
    with open(Path("models/metrics.json"), "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/analytics")
def analytics():
    analytics_file = Path("models/analytics.json")
    if analytics_file.exists():
        return json.loads(analytics_file.read_text(encoding="utf-8"))
    return compute_analytics()


@app.get("/random_sample")
def random_sample():
    df = pd.read_csv("data/agri_dataset.csv")
    return df.sample(1).to_dict(orient="records")[0]
