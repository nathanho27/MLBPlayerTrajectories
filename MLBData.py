from pybaseball import statcast
import pandas as pd
import numpy as np
import os

Seasons = []

# Pull regular-season Statcast batter data (2021–2025)
for Season in range(2022, 2026):
    print(f"Pulling Statcast data for {Season}")

    SeasonData = statcast(
        start_dt=f"{Season}-03-20",
        end_dt=f"{Season}-10-05",  # regular season only
    )

    SeasonData["Season"] = Season
    Seasons.append(SeasonData)

StatcastRaw = pd.concat(Seasons, ignore_index=True)

os.makedirs("data/raw", exist_ok=True)
StatcastRaw.to_csv(
    "data/raw/StatcastBatter_2022_2025.csv",
    index=False
)

print(f"Rows: {StatcastRaw.shape[0]}")