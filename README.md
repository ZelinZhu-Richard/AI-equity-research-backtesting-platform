````markdown
# AI Equity Research and Backtesting Platform

This project is a reproducible equity research and backtesting platform built to turn raw market data into timestamp-safe features, baseline models, walk-forward predictions, portfolio backtests, and clear research reports.

The first version is a 14-day, 42-hour sprint. The long-term version is a 300+ hour flagship proof-of-work project for quant development and ML research engineering.

## What It Will Be

At maturity, this platform will take a small equity universe through the full research workflow:

```text
raw equity data
  -> data validation
  -> clean SQL/parquet tables
  -> timestamp-safe feature generation
  -> baseline and ML model training
  -> walk-forward prediction
  -> cost-aware portfolio backtest
  -> risk/performance report
  -> research memo
```

The goal is not to claim a profitable strategy. The goal is to show disciplined research engineering: clean data, reproducible scripts, honest validation, and clear communication of results.

## First Hiring Gate

The first target is Poesis Founding Quant Developer.

This repo is designed to show:

- clean Python project structure
- reproducible setup
- financial data ingestion
- SQL/parquet data layer
- feature generation scripts
- baseline model evaluation
- walk-forward backtesting
- clear experiment reports

Later versions can extend toward Poesis Founding ML Engineer and HRT-style quant research by adding stronger validation, more models, portfolio risk analysis, and deeper failure-mode studies.

## What Makes This Stand Out

Most student finance projects stop at a notebook and a pretty backtest. This project is designed to be stronger because it emphasizes:

- **Reproducibility**: installable package, stable commands, and generated reports.
- **Data discipline**: raw and processed data are separated, schemas are documented, and validation checks run before modeling.
- **Timestamp safety**: features are designed to avoid lookahead bias.
- **Baseline-first modeling**: naive and simple models come before complex ML.
- **Realistic backtesting**: portfolio results include transaction costs, turnover, drawdown, and risk metrics.
- **Research communication**: each experiment should produce a memo explaining setup, result, limitation, and next action.

## What This Is Not

This is not a live trading system.
This is not a claim of profitable alpha.
This is not a notebook-only project.
This is not high-frequency trading infrastructure.

## Repository Structure

```text
data/
  raw/                Raw downloaded data, ignored by Git
  processed/          Clean tables, DuckDB database, generated parquet files

reports/              Dataset cards, validation summaries, charts, research memos
logs/                 Optional local run logs

src/aerbp/
  config.py           Central paths and project settings
  logging_utils.py    Shared logging helper
  cli.py              Command-line entry points

  data/
    universe.py       Starter equity universe
    ingest.py         Data download/load scripts
    storage.py        DuckDB/parquet table helpers
    validate.py       Data quality checks

  features/
    price_features.py Timestamp-safe return, momentum, volatility, and liquidity features
    targets.py        Forward-return prediction targets

  models/
    baseline.py       Naive and simple baseline predictors
    sklearn_models.py Linear/tree model training

  backtest/
    walk_forward.py   Rolling train/test evaluation
    portfolio.py      Signal-to-portfolio conversion
    metrics.py        Sharpe, drawdown, turnover, hit rate

  reports/
    make_report.py    Markdown report generation

tests/                Smoke tests and unit tests
```

## Current Sprint Goal

The 14-day sprint should produce:

- daily OHLCV ingestion for a small U.S. equity universe
- raw and clean local data tables
- dataset card and validation summary
- at least 10 timestamp-safe features
- one forward-return target
- naive baseline model
- one simple sklearn model
- walk-forward predictions
- cost-aware portfolio backtest
- final sprint report with limitations

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Day 1 Checks

```bash
aerbp-info
pytest
```

## Expected Day 1 Output

Day 1 is complete when:

- the package installs with `pip install -e .`
- `aerbp-info` prints project configuration
- `pytest` passes
- the README explains the project structure and research standard

## Expected Structure

```text
data/raw/           raw downloaded data
data/processed/     clean tables and DuckDB database
reports/            generated reports and charts
logs/               run logs
src/aerbp/          Python package
tests/              smoke tests and unit tests
```

## Current Status

- Day 1: project skeleton, config, CLI, logging, tests
- Day 2 next: equity universe and raw data ingestion

## Development Standard

Every major step should leave behind three things:

1. runnable code
2. a saved artifact
3. a short written explanation

If a result cannot be reproduced, it does not count. If a model beats a baseline but fails after costs, say that directly. If a feature might leak future information, remove it or document the risk before using it.
````
