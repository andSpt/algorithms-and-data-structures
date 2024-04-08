import pytest

from structures.brakes_in_code import check_brackets


@pytest.mark.parametrize('string, expected_result', [
    ("([](){([])})", 'Success'),
    ("{*}", 'Success'),
    ("{}", 'Success'),
    ("", 'Success'),
    ("*{}", 'Success')
])
def test_brakes_in_code_correct(string, expected_result):
    assert check_brackets(string) == expected_result

@pytest.mark.parametrize('string, expected_result', [
    ("()[]}", 5),
    ("{{[()]]", 7),
    ("{{{[][][]", 3),
    ("{*{{}", 2),
    ("[[*", 2),
    ("{{", 2),
    ("}", 1),
    ("{{{**[][][]", 3)
])
def test_brakes_in_code_wrong(string, expected_result):
    assert check_brackets(string) == expected_result


