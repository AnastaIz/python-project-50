from gendiff import generate_diff


def test_flat_json():
    diff_file1_file2 = generate_diff('/Users/anastasiaizmaylova/python-project-50/tests/fixtures/file1.json',
                                    '/Users/anastasiaizmaylova/python-project-50/tests/fixtures/file2.json')
    correct_diff = open('/Users/anastasiaizmaylova/python-project-50/tests/fixtures/flat_json.txt')
    assert diff_file1_file2 == correct_diff.read()