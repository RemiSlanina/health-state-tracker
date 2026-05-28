# Health State Tracker

Small learning project exploring structured tracking of health-related states such as energy, pain, sensory load, and daily observations.

The project is intended as a lightweight backend-focused application for experimenting with:

* PostgreSQL
* Python
* relational database design
* backend architecture
* data persistence
* accessibility-oriented design ideas

## Current Goals (V1)

The initial version focuses on keeping scope intentionally small.

Planned features:

* create health state entries
* store entries in PostgreSQL
* track:

  * energy level
  * pain level
  * sensory load
  * food tolerance
  * notes/free text observations
* retrieve and display stored entries

The project is designed around low-friction input and simple structure rather than complex analytics.

## Motivation

The idea emerged from an interest in structured state tracking during periods of cognitive overload, fatigue, or reduced communication ability.

Many existing trackers assume high energy, high executive function, or complex interaction patterns. This project explores simpler and more accessible approaches.

## Planned Future Ideas

Possible future extensions may include:

* search/filter functionality
* tagging system
* temporal pattern analysis
* symptom/state correlations
* FastAPI backend
* expanded tracking
* frontend/mobile interface
* data visualization
* export/import functionality

These are exploratory ideas and not part of the current scope.

## Tech Stack

Current:

* Python
* PostgreSQL
* psycopg
* PyCharm
* DataGrip

Planned / exploring:

* FastAPI
* SQLAlchemy

## Project Structure

```text
health-state-tracker/
│
├── app/
├── notes/
├── dev-notes/
├── README.md
├── requirements.txt
└── schema.sql
```

## Notes

This is primarily a learning project focused on backend concepts and iterative development.
