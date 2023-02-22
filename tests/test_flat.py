from gendiff import generate_diff


def test_flat():
    diff_json_files = generate_diff('tests/fixtures/file1.json',
                                    'tests/fixtures/file2.json')
    diff_yaml_files = generate_diff('tests/fixtures/file1.yaml',
                                    'tests/fixtures/file2.yaml')
    correct_diff = open('tests/fixtures/flat_json.txt').read()
    assert diff_json_files == correct_diff
    assert diff_yaml_files == correct_diff
