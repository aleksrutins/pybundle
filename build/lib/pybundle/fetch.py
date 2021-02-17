import requests

def fetch(url: str) -> str:
    response = requests.get("https://pypi.org/simple/")
    response.raise_for_status()
    return response.text