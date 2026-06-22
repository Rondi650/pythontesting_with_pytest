from pathlib import Path
from unittest import mock


def home_dir():
    print(str(Path.home()))
    return str(Path.home())


def test_mock_home():
    with mock.patch('pathlib.Path.home', return_value='/users/fake_user') as t:
        assert home_dir() == t.return_value


def test_path_home_is_called():
    with mock.patch('pathlib.Path.home') as mock_home:
        mock_home.return_value = Path('/users/fake_user')
        home_dir()
        mock_home.assert_called()


def test_home_dir_calls_path_home_without_mock():
    """Testa que home_dir retorna o mesmo que Path.home() sem usar mock"""
    assert home_dir() == str(Path.home())


if __name__ == "__main__":
    print(home_dir())
