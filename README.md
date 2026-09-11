# API to CSV Tool

A Python 3.11+ CLI that fetches user records from a JSON API and exports selected fields to CSV.

## Run

```bash
python -m pip install -r requirements.txt
python -m src.main https://jsonplaceholder.typicode.com/users data/users.csv
```

Columns: `id`, `name`, `username`, `email`, `phone`, `website`, `city`, `company`.

The mapping expects user records with nested address and company fields, not arbitrary JSON. Invalid responses are reported, and output directories are created automatically.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
