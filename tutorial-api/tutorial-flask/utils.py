import json


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def load_config(path=None):
    if path == None:
        path = "config.json"
    config: dict = read_json(path)
    return config