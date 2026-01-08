from pybaseball import fg_batting_data
import pandas as pd
import numpy as np
import os

Seasons = []

# Pull FanGraphs season-level batting data (2022–2025)
for Season in range(2022, 2026):
    print(f"Pulling FanGraphs batting data for {Season}")

    SeasonData = fg_batting_data(Season)
    SeasonData["Season"] = Season
    Seasons.append(SeasonData)

FanGraphsRaw = pd.concat(Seasons, ignore_index=True)

os.makedirs("data/raw", exist_ok=True)
FanGraphsRaw.to_csv(
    "data/raw/FanGraphsBatting_2022_2025.csv",
    index=False
)

print(f"Rows: {FanGraphsRaw.shape[0]}")