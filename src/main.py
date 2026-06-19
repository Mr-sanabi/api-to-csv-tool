import argparse
import logging
from api_client import fetch_users
from transformer import extract_user_row, extract_user_rows
from storage import save_csv
from logger_config import setup_logging


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("api_url")
    parser.add_argument("output_file")
    return parser.parse_args()

def main():
    setup_logging()

    logging.info("API to CSV tool started")
    args = parse_args()

    users = fetch_users(args.api_url)

    if users is None:
        return 

    if not isinstance(users, list):
        logging.error("Invalid API response: expected list")
        return
    
    if not users:
        logging.warning("API returned empty user list")
        return

    rows = extract_user_rows(users)

    save_csv(args.output_file, rows)

    summary = (
        "API to CSV tool summary\n"
        f"Users fetched: {len(users)}\n"
        f"Rows exportd: {len(rows)}\n"
        f"Output file: {args.output_file}\n"
        )

    logging.info(summary)

if __name__ == "__main__":
    main()