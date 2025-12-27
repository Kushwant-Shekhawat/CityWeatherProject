from src.config import DEFAULT_TIMEOUT
import requests

def get_call(url, params):
    response = requests.get(url, params = params,timeout=DEFAULT_TIMEOUT)
    if response.status_code != 200:
        raise RuntimeError(f"API call failed with : {response.status_code}. URL : {response.url}")
    return response