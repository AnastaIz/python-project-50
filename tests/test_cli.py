from gendiff.cli import parse_args_cli


def test_cli():
    paths = parse_args_cli(['tests/fixtures/file1.json', 'tests/fixtures/file2.json'])
    assert paths.first_file == 'tests/fixtures/file1.json'
    assert paths.second_file == 'tests/fixtures/file2.json'
    assert paths.format == 'stylish'
