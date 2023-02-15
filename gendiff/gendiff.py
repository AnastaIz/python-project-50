from data_parser import open_file
import itertools


def generate_diff(file_path1, file_path2, replacer='  '):
    data1 = open_file(file_path1)
    data2 = open_file(file_path2)

    keys = sorted(data1.keys() | data2.keys())
    result = []
    for key in keys:
        if key not in data1:
            result.append(replacer + f'+ {key}: {data2[key]}'.lower())
        elif key not in data2:
            result.append(replacer + f'- {key}: {data1[key]}'.lower())
        elif data1[key] == data2[key]:
            result.append(replacer + f'  {key}: {data1[key]}'.lower())
        else:
            result.append(replacer + f'- {key}: {data1[key]}'.lower())
            result.append(replacer + f'+ {key}: {data2[key]}'.lower())
    return '\n'.join(itertools.chain("{", result, "}"))
