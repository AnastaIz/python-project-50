from gendiff.data_parser import open_file
from gendiff.diff import diff
from gendiff.stylish import stylish
from gendiff.plain import plain


def generate_diff(file_path1, file_path2, format):
    data1 = open_file(file_path1)
    data2 = open_file(file_path2)

    if format == 'plain':
        return plain(diff(data1, data2))
    else:
        return stylish(diff(data1, data2))
