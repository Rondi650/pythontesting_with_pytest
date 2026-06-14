def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


def testcomparando_contas():
    conta1 = 1+2+3+4+5
    conta2 = 5+4+3+2+1.1
    assert conta1 == conta2


def test_comparando_strings():
    string1 = 'python'
    string2 = 'Python'
    assert string1 == string2
