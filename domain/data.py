import json
import logging
from urllib.request import urlopen


def find(url: str):
    """
    Connect to the public url to get data in json format
    :param url: Url that will be used to find data
    :return: A json result of call
    """
    try:
        response = urlopen(url)
        data = json.loads(response.read())
        return data
    except Exception as e:
        logging.error("Can't find data from url: ", url)
        raise e
