# MLBPlayerTrajectories

Statcast-based modeling of MLB player performance trajectories, identifying breakout, bounceback, decline, and stable profiles with interpretable machine learning and Power BI visualization.

---

## Status

Planned (Post-YelpBI)

---

## Overview

MLBPlayerTrajectories is a modeling-focused analytics project that studies how MLB hitters transition between different performance states over time. Rather than treating player performance as static, the project frames offense as a **trajectory problem**, using Statcast tracking data to predict future outcomes.

The primary objective is to identify players likely to experience meaningful changes in offensive performance, such as breakouts, bouncebacks, or declines, using only information available before the prediction season. Results are designed to be interpretable and consumable through a lightweight Power BI dashboard.

---

## Trajectory Definitions

Player trajectories are defined using **season-level OPS+**, a park- and league-adjusted offensive metric. Labels are constructed using a multi-year context to avoid noise and short-term fluctuations.

* **Breakout**: Transition from average or below-average production to clearly above-average performance
* **Bounceback**: Return to prior strong performance following a down season
* **Decline**: Sustained drop from previous offensive levels
* **Stable**: Performance remains within expected ranges

OPS+ is used strictly for labeling, while model features rely entirely on prior-season Statcast data to prevent leakage.

---

## Data Sources

* **Baseball Savant / Statcast**: Pitch-level tracking data aggregated to the player-season level
* **Season-Level OPS+**: Used exclusively for trajectory labeling

---

## Feature Engineering

Features are engineered to capture **offensive process**, not results, and are aggregated at the player-season level.

### Contact Quality

* Expected wOBA (xwOBA)
* Average exit velocity
* Barrel percentage
* Hard-hit rate
* Sweet spot percentage

### Plate Discipline

* Chase rate
* Whiff rate
* Zone swing percentage
* BB% minus K%

### Batted Ball Profile

* Pull rate
* Fly ball rate
* Ground ball rate
* Pull-air rate

### Context & Trends

* Year-over-year deltas in key Statcast metrics
* Rolling multi-season averages
* Age and playing-time controls

---

## Modeling Approach

Each trajectory type is modeled independently using binary classification.

* Logistic regression for baseline interpretability
* Tree-based models to capture nonlinear effects
* Feature importance and SHAP-style explanations

Evaluation emphasizes precision, recall, and ranking quality, reflecting how analysts identify a small set of high-upside or high-risk players.

---

## Visualization

Model outputs are translated into a **Power BI dashboard** designed to support ranking and interpretation rather than raw data exploration.

Dashboard views include:

* Ranked breakout and bounce-back candidates
* Player-level driver explanations
* Trajectory outcome comparisons

---

## Project Structure

```
MLBPlayerTrajectories/
├── notebooks/
│   ├── 01_data_pull.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_label_construction.ipynb
│   ├── 04_breakout_model.ipynb
├── data/
│   ├── raw/
│   ├── processed/
├── README.md
```

---

## Planned Work

After completing my current slate of projects, this repository will be initialized with data ingestion, feature engineering, and a first-pass breakout model. Additional trajectory types and dashboard enhancements will be added iteratively.

---

## Why This Project

While grounded in baseball, this project mirrors real-world analytics problems such as lifecycle modeling, risk identification, and performance forecasting. The emphasis is on clean labeling, interpretable modeling, and clear communication of results rather than production deployment.

