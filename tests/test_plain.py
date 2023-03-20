from gendiff.open_file import open_file
from gendiff.diff import diff
from gendiff.formatters.plain import plain


def test_plain():
    flat_data1 = open_file('tests/fixtures/file1.json')
    flat_data2 = open_file('tests/fixtures/file2.json')
    flat_diff = diff(flat_data1, flat_data2)
    flat_result = open('tests/fixtures/flat_data_plain.txt').read()

    nested_data1 = open_file('tests/fixtures/nested_file1.yml')
    nested_data2 = open_file('tests/fixtures/nested_file2.yml')
    nested_diff = diff(nested_data1, nested_data2)
    nested_result = open('tests/fixtures/nested_data_plain.txt').read()

    assert plain(flat_diff) == flat_result
    assert plain(nested_diff) == nested_result
