# Marriott Monarch Availability Agent

This repo contains a starter agent that monitors availability for the 3 bedroom suite at Marriott's Monarch at Sea Pines on Hilton Head.

## What it does

- opens Marriott's booking flow with Playwright
- checks a configurable set of stay windows
- looks for room names that match the 3 bedroom suite or penthouse
- stores state locally so it only alerts on changes
- can run locally or on a schedule in GitHub Actions

## Project layout

- `src/monarch_agent/config.py` configuration and environment handling
- `src/monarch_agent/models.py` typed models
- `src/monarch_agent/state.py` local state persistence
- `src/monarch_agent/notifier.py` email alerting
- `src/monarch_agent/marriott_checker.py` browser automation and parsing
- `src/monarch_agent/main.py` agent entrypoint
- `.github/workflows/monitor.yml` scheduled job

## Setup

1. Create a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Install Playwright browsers with `playwright install chromium`.
4. Copy `.env.example` to `.env` and fill in values.
5. Run `python -m src.monarch_agent.main`.

## Important note

Marriott booking pages can change. This project includes a strong starter architecture, but selectors may need tuning after a real run against the live booking page.
