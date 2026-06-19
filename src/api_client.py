import requests
import logging

def fetch_users(url):
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None
    
    if response.status_code != 200:
        logging.error(f"Bad status code: {response.status_code}")
        return None
    
    logging.info(f"Page fetch successfully: {url}")
    return response.json()
        