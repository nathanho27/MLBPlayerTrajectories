# Feature Context: Cleaned Player–Season Dataset

This document describes the columns retained after SQL-based cleaning and staging.
The goal of the dataset is to support **forward-looking modeling of year-over-year
offensive performance change**, while minimizing team and contextual noise.

Columns are grouped by their analytical role and baseball intuition.

---

## Identifiers and Structure

These fields are required for grouping, ordering, and downstream visualization.
They are not used as predictive inputs.

- **IDfg**  
  Unique FanGraphs player identifier used for joins and season alignment.

- **Name**  
  Player name for interpretability and dashboard use.

- **Season**  
  Season indicator used to construct lagged features and year-over-year deltas.

---

## Demographics and Opportunity Context

These variables provide structural context and help control for aging and role effects.

- **Age**  
  Captures aging curves, physical decline risk, and reduced breakout likelihood at older ages.

- **G (Games Played)**  
  Indicates role stability and sample size. Used to assess reliability rather than drive predictions.

- **PA (Plate Appearances)**  
  Controls for exposure and filters extreme small-sample noise.

---

## Offensive Outcome Metrics (Targets, Not Inputs)

These metrics describe *what happened* rather than *why it happened*.
They are used for labeling, evaluation, and interpretation — not as model features.

- **wRC+**  
  Park- and league-adjusted offensive production metric.  
  This is the primary outcome used to define year-over-year change.

- **WAR**  
  Overall value metric included for context and dashboard use, not modeling.

---

## Expected Performance and Variance Indicators

These metrics help separate underlying skill from short-term variance.

- **xwOBA**  
  Expected weighted on-base average based on contact quality.  
  Useful for identifying potential regression or underperformance.

---

## Plate Discipline and Bat-to-Ball Skill

These features capture approach and contact ability, often leading indicators of
future improvement or decline.

- **BB% (Walk Rate)**  
  Reflects strike-zone control and patience.

- **K% (Strikeout Rate)**  
  High or rising strikeout rates limit offensive upside and often precede decline.

- **BB/K**  
  Compact and interpretable summary of plate discipline.

- **O-Swing%**  
  Chase rate on pitches outside the strike zone.  
  Increases may signal erosion in discipline.

- **Z-Contact%**  
  Contact rate on pitches inside the zone.  
  Declines may reflect bat speed loss or timing issues.

- **SwStr% (Swinging Strike Rate)**  
  Stable indicator of whiff tendency, closely tied to strikeout behavior.

---

## Contact Quality and Power Indicators

These metrics describe how hard and how efficiently the ball is struck.

- **EV (Average Exit Velocity)**  
  Proxy for bat speed and raw contact strength.

- **maxEV**  
  Peak exit velocity indicating remaining top-end power potential.

- **HardHit%**  
  Share of batted balls struck at high velocity, reflecting consistency of hard contact.

- **Barrel%**  
  Measures optimal exit velocity and launch angle combinations.  
  Often a strong signal of power-driven breakouts.

- **LA (Launch Angle)**  
  Describes batted-ball shape. Changes can drive breakouts or declines but are noisy.

---

## Modeling Perspective

The dataset is structured to support **prediction of year-over-year change in wRC+**,
not absolute performance levels.

- Outcome metrics define the target variable.
- Process-level metrics serve as predictive inputs.
- Trajectory labels (breakout, decline, bounceback, stable) are derived *after* modeling
  using analyst-defined thresholds to preserve flexibility and interpretability.

This separation mirrors real-world performance forecasting workflows and helps prevent
information leakage.