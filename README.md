# MLBPlayerTrajectories

Season-level modeling of MLB hitter performance trajectories, identifying breakout, bounceback, decline, and stable profiles using interpretable machine learning.

---

## Status

**In Progress**

---

## Overview

MLBPlayerTrajectories is a modeling-focused analytics project that studies how MLB hitters transition between different performance states over time. Rather than treating player performance as static, the project frames offense as a **trajectory problem**, using historical season-level performance to forecast future outcomes.

The primary objective is to identify players likely to experience meaningful changes in offensive performance, such as breakouts, bouncebacks, or declines, using only information available **prior to the prediction season**.

---

## Trajectory Definitions

Player trajectories are defined using season-level offensive performance metrics, with labels constructed in a multi-year context to reduce noise and short-term volatility.

- **Breakout**: Transition from average or below-average production to clearly above-average performance  
- **Bounceback**: Return to prior strong performance following a down season  
- **Decline**: Sustained drop from previous offensive levels  
- **Stable**: Performance remains within expected historical ranges  

Labels are derived from future season outcomes, while all modeling inputs are restricted to prior-season information to prevent information leakage.

---

## Data Sources

- **FanGraphs (via pybaseball)**  
  Season-level hitter statistics including plate appearances, wRC+, ISO, BB%, K%, and related offensive metrics.

Data is accessed programmatically using `pybaseball` and stored locally for reproducibility and downstream analysis.

---

## Modeling Approach

The project follows a clean, forward-looking backtesting framework designed to evaluate how hitter performance changes across seasons:

- Player–season data is structured chronologically to prevent information leakage  
- Features are derived from prior-season and multi-season trends in offensive process metrics  
- Future-season performance is held out to evaluate predicted change  

The modeling task is framed as a regression problem that estimates expected change in offensive performance, rather than directly predicting trajectory labels. Predicted changes are then mapped into interpretable trajectory outcomes such as breakout, decline, bounceback, or stability using analyst-defined thresholds.

Baseline models emphasize interpretability and ranking quality, allowing clear inspection of drivers behind projected improvement or decline. More complex models are treated as extensions rather than the core objective.
---

## Data Storage & Workflow

Season-level data is staged in **MySQL** to support clean, reproducible analytical transformations and dataset versioning. Python is used for exploration, modeling, and evaluation after data is structured relationally.

---

## Project Structure

```
MLBPlayerTrajectories/
├── MLBData.py
│
├── notebooks/
│   ├── 01ExploreData.ipynb
│   ├── 02StagePlayerSeason.ipynb
│   ├── 03MLModel.ipynb
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── README.md

```
## Visualization

Model outputs will be translated into a **Power BI dashboard** designed for interpretation and decision support rather than raw data exploration.

Planned views include:
- Ranked breakout and bounceback candidates
- Player-level trajectory summaries
- Comparisons between predicted and realized outcomes

The visualization layer is intended to make model results accessible to non-technical stakeholders while preserving analytical context.

---

## Planned Work

- Finalize player-season dataset construction
- Develop and validate trajectory labels
- Train and evaluate classification models
- Build Power BI dashboard for result interpretation

---

## Why This Project

While grounded in baseball, this project mirrors real-world analytics problems such as lifecycle modeling, risk identification, and performance forecasting. The emphasis is on clear problem framing, defensible evaluation, and interpretable modeling decisions rather than heavy data engineering or production systems.

