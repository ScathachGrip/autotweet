import requests
import json
import random
import string

def better_object(parser: dict):
    return json.dumps(parser, sort_keys=True, indent=4, ensure_ascii=False)

def deserialize(data: list):
    return json.loads(better_object(data), encoding="utf-8")

async def fetch(target: str):
    """Fetches the data from the target
    Parameters
    ----------
    target : str
        The target URL
    Returns
    -------
    list
        The raw data
    """
    return requests.get(target).json()

def hack() -> str:
    a = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(12)])
    return f"FGO{a}"