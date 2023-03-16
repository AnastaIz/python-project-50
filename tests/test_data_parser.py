import pytest
from gendiff.data_parser import open_file


def test_open_file():
    result = {
            'host': 'hexlet.io',
            'timeout': 50,
            'proxy': '123.234.53.22',
            'follow': False
            }
    path_to_json_file = 'tests/fixtures/file1.json'
    path_to_yaml_file = 'tests/fixtures/file1.yaml'
    path_to_other_format_file = 'tests/fixtures/flat_json.txt'

    assert open_file(path_to_json_file) == result
    assert open_file(path_to_yaml_file) == result

    with pytest.raises(ValueError):
        open_file(path_to_other_format_file)
