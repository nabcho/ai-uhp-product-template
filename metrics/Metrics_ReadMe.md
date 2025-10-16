# 📊 AI-UHP_GF-SE + DC&R — Metrics Logging Guide

## Purpose
To support the continuous feedback loop between Nabil (operator) and the AI core.
Logs capture operational + financial performance for weekly AI analysis.

## File Structure
/metrics/
 ├─ weekly_metrics.csv      # Raw weekly logs
 └─ Metrics_ReadMe.md       # This documentation

## Logging Schedule
- **Frequency:** Once per week (Sunday recommended)
- **Duration:** Permanent, from first sale onward
- **Format:** Append one line per week to `weekly_metrics.csv`

## Fields Summary
| Field | Description | Example |
|-------|--------------|---------|
| Week | ISO date (week end) | 2025-12-07 |
| SaaS_Rev | SaaS & tool income (€) | 450 |
| Data_Rev | Dataset/API income (€) | 80 |
| Hours | Time worked | 26 |
| Support_Tickets | Issues handled | 2 |
| API_Calls | Automated workload | 1500 |
| Visitors | Site traffic | 950 |
| Errors | Failed jobs | 1 |
| Notes | Free text | “Added DC&R collector v0.2” |

## Operational Notes
- Until you have real sales, **do not log dummy data** — the first line should reflect genuine activity.
- Back-fill any missing weeks later; consistency is more important than real-time precision.
- Keep all currency values in **EUR**.

## Next Step
When the first revenue or dataset event occurs (≈ Day 25–30),
start logging weekly and share the updated CSV here for analysis.
