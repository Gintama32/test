from next import msg
import pytest


def test_next(capsys):
    msg()
    captured = capsys.readouterr()
    assert captured.out == "Successfully called the next file function\n"
