# API to CSV Tool

A focused Python CLI that downloads user records from a JSON API, maps nested fields, and exports a clean CSV file.

## Features

- request timeout and HTTP-status validation;
- safe extraction of nested address and company fields;
- graceful handling of invalid JSON and unexpected response shapes;
- automatic creation of output and log directories;
- deterministic CSV schema.

## Usage

```bash
python -m pip install -r requirements.txt
python -m src.main https://jsonplaceholder.typicode.com/users data/users.csv
```

## Exported fields

`id`, `name`, `username`, `email`, `phone`, `website`, `city`, `company`.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Stack

Python 3.11+, Requests, argparse, CSV, logging, pytest.
