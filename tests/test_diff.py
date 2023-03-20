from gendiff.open_file import open_file
from gendiff.diff import diff


def test_diff():
    result = {'follow': {'type': 'removed', 'value': False},
              'host': {'type': 'unchanged', 'value': 'hexlet.io'},
              'proxy': {'type': 'removed', 'value': '123.234.53.22'},
              'timeout': {'type': 'updated', 'value1': 50, 'value2': 20},
              'verbose': {'type': 'added', 'value': True}}

    data1 = open_file('tests/fixtures/file1.json')
    data2 = open_file('tests/fixtures/file2.json')

    assert diff(data1, data2) == result
