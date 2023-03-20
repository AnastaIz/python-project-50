import json
from gendiff.diff import diff
from gendiff.formatters.json_f import json_
from gendiff.open_file import open_file


def test_json_f():
    result = diff(
        open_file('tests/fixtures/file1.json'),
        open_file('tests/fixtures/file2.json')
    )
    to_json = json_(result)

    assert json.loads(to_json) == result
