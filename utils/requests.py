import requests
import json
import random
import string

def better_object(parser: dict):
    """Converts the json object to a more readable object.
    Parameters
    ----------
    parser : dict
    Returns
    -------
    dict
        The new dictionaries with neat keys.
    """
    return json.dumps(parser, indent=4, ensure_ascii=False)

def deserialize(data: list):
    """Deserialize instance containing a JSON document
    Parameters
    ----------
    data : list
        The raw data after fetch request
    Returns
    -------
    dict
        The deserialized with better object
    """
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

def gimmick() -> str:
    """Generates post description
    Returns
    -------
    str
        The post description
    """
    content = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(12)])
    return f"FGO{content}"