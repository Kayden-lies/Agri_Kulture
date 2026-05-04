from pathlib import Path
import pandas as pd
from backend.data_engine import generate_sample
from backend.state_data import state_data

def build_dataset(samples_per_state: int = 250, out_file: Path = Path('data/agri_dataset.csv')) -> Path:
    rows = []
    for state in state_data:
        for _ in range(samples_per_state):
            rows.append(generate_sample(state))
    df = pd.DataFrame(rows)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_file, index=False)
    return out_file

if __name__ == '__main__':
    p = build_dataset()
    print(f'Dataset generated: {p}')
