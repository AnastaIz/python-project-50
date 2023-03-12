from gendiff.data_parser import open_file
from gendiff.diff import diff
from gendiff.stylish import stylish


def test_stylish():
    flat_data1 = open_file('tests/fixtures/file1.json')
    flat_data2 = open_file('tests/fixtures/file2.json')
    flat_diff = diff(flat_data1, flat_data2)
    flat_result = open('tests/fixtures/flat_json.txt').read()

    nested_data1 = open_file('tests/fixtures/nested_file1.yml')
    nested_data2 = open_file('tests/fixtures/nested_file2.yml')
    nested_diff = diff(nested_data1, nested_data2)
    nested_result = open('tests/fixtures/nested_json.txt').read()

    assert stylish(flat_diff) == flat_result
    assert stylish(nested_diff) == nested_result
