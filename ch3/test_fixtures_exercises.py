from re import S

import pytest

# fixtures


@pytest.fixture(scope='module')
def test_list():
    '''
    Esse Fixture faz parte do exercio final do capitulo 3
    do livro python testing with pytest3
    Essa fixture testa o retorno de uma lista
    '''
    print("\n", "-"*50)
    print('Dentro da fixture list')
    yield [1, 2, 3]
    print('\nDepois da fixture list')


@pytest.fixture(scope='package')
def test_dict():
    '''
    Esse Fixture faz parte do exercio final do capitulo 3
    do livro python testing with pytest
    Essa fixture testa o retorno de um dicionario
    '''
    print("\n", "-"*50)
    print('Dentro da fixture dict')
    yield {
        "nome": "rondi",
        "idade": 35
    }
    print('\nDepois da fixture dict')


# testes


def test_fixture_list(test_list):
    assert test_list == [1, 2, 3]


def test_failing_fixture_list(test_list):
    assert test_list == []


def test_fixture_dict(test_dict):
    assert test_dict == {
        "nome": "rondi",
        "idade": 35
    }


def test_failing_fixture_dict(test_dict):
    assert test_dict == {}
