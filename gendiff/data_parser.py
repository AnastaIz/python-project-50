import json
import yaml


def open_file(file):
    if str(file).endswith('json'):
        return json.load(open(file))
    elif str(file).endswith('yml') or str(file).endswith('yaml'):
        return yaml.safe_load(open(file))
    else:
        raise ValueError('Invalid file format')
