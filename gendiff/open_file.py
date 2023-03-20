from gendiff.parser import parse


def open_file(file):
    if str(file).endswith('json'):
        type_format = 'json'
    elif str(file).endswith('yml') or str(file).endswith('yaml'):
        type_format = 'yaml'
    else:
        type_format = 'other'
    data = open(file).read()
    return parse(data, type_format)
