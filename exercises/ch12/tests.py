import sums
import subprocess


def test_sum():
    soma = subprocess.run(['python', 'sums.py'],
                          capture_output=True, text=True)
    result = soma.stdout.strip()
    assert result == 200
