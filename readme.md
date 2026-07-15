# AI-Powered Rubik's Cube Solver (Scaffold)

This repository currently contains only the initial project structure for a professional Flask-based web application.

No solver or application functionality has been implemented yet.

## Tech Stack (Planned)

- Python 3.12
- Flask (backend)
- HTML, CSS, JavaScript (frontend)

## Project Structure

```text
.
|-- app.py
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- models/
|   |   `-- __init__.py
|   |-- routes/
|   |   `-- __init__.py
|   |-- services/
|   |   `-- __init__.py
|   |-- static/
|   |   |-- css/
|   |   |   `-- main.css
|   |   `-- js/
|   |       `-- main.js
|   `-- templates/
|       |-- base.html
|       `-- index.html
`-- tests/
	`-- __init__.py
```

## Virtual Environment Setup (Python 3.12)

### Windows (PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS/Linux (bash/zsh)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Incremental Build Plan

This project will be implemented in incremental steps. Current step: project scaffolding only.