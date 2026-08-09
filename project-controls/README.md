# Fire Fighting System — New DC · Installation Schedule & Responsibility Tracker

**Deliverable:** `Fire-Fighting-System-New-DC_Installation-Schedule_v0.1.xlsx`
**Version:** 0.1 — Preliminary Planning Baseline
**Source document:** RC Vehicle Survey Report – Fire Fighting System for New DC, dated **30-Jun-2026**

A management-ready project-control workbook derived from the survey report. It is not a
reproduction of the survey — it turns the survey's findings into a trackable schedule covering
**WHAT → WHEN → WHO → OWNER → DEPENDENCY → STATUS → RISK → COMPLETION**.

> This folder is a standalone project-planning deliverable and is unrelated to the application
> code in this repository.

## Workbook contents

| Sheet | Purpose |
|---|---|
| 1. Exec Dashboard | Executive summary, live KPIs, the two confirmed constraints, 13 milestones, critical-path actions, status key |
| 2. Master Schedule | 49 activities across 6 phases, plus the Critical Dependencies & Constraints table |
| 3. Gantt Chart | Relative Week 1–18 proposed baseline, colour-coded by phase, with critical and Trailer-2 bars |
| 4. Responsibility Matrix | Governance block + 14 responsibility areas |
| 5. Action Tracker | 12 management actions ordered by ability to delay installation |
| 6. Risk Register | 10 risks with auto-calculated risk rating |
| 7. Document Control | Document metadata, revision history, source traceability |

## What is confirmed vs. what is proposed

The workbook keeps these strictly separate. **Confirmed by the survey** — and nothing else — is:

- Project: Fire Fighting System for New DC; asset: Mobile / Trailer-based DC
- Survey date: 30-Jun-2026
- Project Manager: Kharsan Mujeb Al Ajmi (the only person named in the source)
- Installation of Racks and Cabinets has not yet started in the available trailers
- The power source in Trailer-2 is currently unavailable because partition works are still ongoing
- The survey recommends providing a Fire Alarm System and a Fire Suppression System

Rows carrying source-supported facts are tagged `CONFIRMED (SURVEY)` in the Remarks column.
Everything else is a proposed planning value or a `TBC` / `TBD` placeholder — the workbook
contains **280 TBC** and **144 TBD** markers and exactly **two date cells**, both holding the
source-confirmed survey date.

No start, duration or completion dates are stated in the source, so none are asserted. The
Gantt is a **relative** Week 1–18 baseline (Week 1 = kickoff), labelled
*PROPOSED BASELINE — DATES TO BE CONFIRMED* on the sheet itself.

## Built-in automation

Formulas (163 in total, all verified to evaluate without errors):

- **Duration** — `Planned Finish − Planned Start + 1`, or `TBD` while either date is empty
- **Days Remaining** — days to finish, `Closed` once complete, `TBD` while undated
- **Schedule Flag** — resolves in priority order to `COMPLETE`, `OVERDUE`, `BLOCKED`,
  `PENDING POWER AVAILABILITY`, `PENDING PREDECESSOR` (via an INDEX/MATCH on the predecessor's
  status), `PENDING APPROVAL` / `PENDING MATERIAL`, `IN PROGRESS`, `READY TO START`, `ON PLAN`
- **Dashboard KPIs** — activity counts by status and overall % complete, aggregated live
- **Risk Rating** — derived from Probability × Severity
- Conditional formatting drives all RAG colouring and the Gantt bars, so bars redraw when the
  baseline week numbers are edited

Drop-down lists are attached to Status, Priority, Approval Required, Probability/Severity and
Risk Status. Shaded cells with blue text are the editable fields for the project team.

## Known gaps

- **No logo.** No official stc/RCS brand asset was available to this build, so the header
  carries the placeholder `[OFFICIAL LOGO — TO BE INSERTED]` rather than a fabricated mark.
  Replace it in the header band of each sheet.
- **The source PDF was not readable in the build environment.** The workbook was built from the
  survey facts as restated in the task brief; the six confirmed items listed above should be
  re-checked against the PDF before the baseline is frozen at Version 1.0.

## Regenerating

```bash
pip install openpyxl
python3 generator/build.py Fire-Fighting-System-New-DC_Installation-Schedule_v0.1.xlsx
```

`generator/data.py` holds all schedule content and is the single place to edit activities,
milestones, actions, risks and dependencies. `generator/common.py` holds the palette and styles.
After regenerating, recalculate with LibreOffice so cached formula values are written:

```bash
python3 /root/.claude/skills/xlsx/scripts/recalc.py <file>.xlsx 360
```
