# API to CSV Tool

A small Python CLI tool that fetches user data from a public API, extracts selected fields, flattens nested JSON values, and exports the result to a CSV file.

## Features

- Fetches data from a public API
- Parses JSON response
- Extracts selected user fields
- Flattens nested fields such as address.city and company.name
- Exports clean data to CSV
- Logs execution summary
- Handles failed requests and invalid API responses

## Tech Stack

- Python
- requests
- argparse
- csv
- logging

## Usage

python src/main.py <api_url> <output_file>

## Example:

python src/main.py https://jsonplaceholder.typicode.com/users data/output_users.csv

## Output columns

id, name, username, email, city, company, website

## Example output

The tool creates a CSV file with cleaned user records from the API.

## What I practiced

- Working with API responses
- Reading JSON data
- Accessing nested dictionaries
- Transforming data into flat rows
- Exporting data to CSV
- Building a small CLI tool