from gendiff.open_file import open_file
from gendiff.diff import diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_f import json_


def generate_diff(file_path1, file_path2, format='stylish'):
    differences = diff(
        open_file(file_path1),
        open_file(file_path2)
    )

    if format == 'plain':
        return plain(differences)
    elif format == 'json':
        return json_(differences)
    else:
        return stylish(differences)
