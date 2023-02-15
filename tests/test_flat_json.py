from gendiff import generate_diff


def test_flat_json():
    diff_file1_file2 = generate_diff('tests/fixtures/file1.json',
                                     'tests/fixtures/file2.json')
    correct_diff = open('tests/fixtures/flat_json.txt').read()
    assert diff_file1_file2 == correct_diff
