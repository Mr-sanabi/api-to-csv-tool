import requests
import logging

def fetch_users(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None
    
    try:
        data = response.json()
    except ValueError as error:
        logging.error(f"Invalid JSON response: {error}")
        return None
    
    logging.info(f"Page fetch successfully: {url}")
    return data
