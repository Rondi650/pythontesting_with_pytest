


from pathlib import Path
import sys


caminho = Path(__file__).parent.parent
print(caminho)

sys.path.append(str(caminho))
from src import hello

def test_full_output():
    assert hello.full_output() == "Hello, World!"


def test_main(capsys):
    hello.main()
    output, _ = capsys.readouterr()
    assert output == "Hello, World!\n"
