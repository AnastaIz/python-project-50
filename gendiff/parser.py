import json
import yaml


def parse(data, type_format):
    if type_format == 'json':
        return json.loads(data)
    elif type_format == 'yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError("Invalid file format")
