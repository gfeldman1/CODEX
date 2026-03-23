# Seasonal monitor settings

Current target behavior:

- scan Marriott Monarch at Sea Pines
- search March through November
- search 5 to 7 night stays
- search both cash and points
- aggressive detection for 3 bedroom related matches
- notify only on new openings
- desired schedule: 0400 UTC and 1600 UTC

Current primary runner:

- `python -m src.monarch_agent.main_openings_only`

GitHub Actions workflow content is intended to run that entrypoint on the above schedule.
