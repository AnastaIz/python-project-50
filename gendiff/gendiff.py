import json
import itertools


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    keys = sorted(data1.keys() | data2.keys())
    result = []
    for key in keys:
        if key not in data1:
            result.append(f'+ {key}: {data2[key]}')
        elif key not in data2:
            result.append(f'- {key}: {data1[key]}')
        elif data1[key] == data2[key]:
            result.append(f'  {key}: {data1[key]}')
        else:
            result.append(f'- {key}: {data1[key]}')
            result.append(f'+ {key}: {data2[key]}')
    return '\n'.join(itertools.chain("{", result, "}"))
