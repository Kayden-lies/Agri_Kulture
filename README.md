# Agri ML Dashboard

Production-ready Agri ML dashboard with FastAPI backend and Leaflet frontend.

## Project Structure
- `backend/`: ML/data pipeline and API modules.
- `frontend/`: HTML/CSS/JS dashboard UI and analytics views.
- `data/`: generated datasets (kept empty in Git; local artifacts only).
- `models/`: generated ML artifacts (kept empty in Git; local artifacts only).

## Clean Reproducible Workflow
1. `pip install -r requirements.txt`
2. `python dataset_builder.py`
3. `python model_engine.py`
4. `uvicorn main:app --reload`

Then open `http://127.0.0.1:8000`.

## API Endpoints
- `POST /predict`
- `GET /metrics`
- `GET /analytics`
- `GET /random_sample`

## Git Hygiene
- Generated datasets (`data/*.csv`) are ignored.
- Trained model binaries (`models/*.pkl`) are ignored.
- Python cache files are ignored.
- `data/.gitkeep` and `models/.gitkeep` preserve folder structure.
