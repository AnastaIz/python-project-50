from gendiff.data_parser import open_file
from gendiff.diff import diff
from gendiff.stylish import stylish


def generate_diff(file_path1, file_path2):
    data1 = open_file(file_path1)
    data2 = open_file(file_path2)

    return stylish(diff(data1, data2))
