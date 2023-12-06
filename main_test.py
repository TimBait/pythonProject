import pytest
from main import archive_string, restore_string

def test_archive_string():
    assert archive_string('qqqwwweeerty') == "q3w3e3rty"
    assert archive_string('qwweeerrrrttttty') == "qw2e3r4t5y"
    assert archive_string('ggghhhtttrrrqwerty') == "g3h3t3r3qwerty"
    assert archive_string('gnnnnnnnnnnbbbbbbbbbbbbbbb') == "gn10b15"
    assert archive_string('qwertyyy') != "q1w1e1r1t1y3"
    assert archive_string('     ggggg') != "     5g5"

def test_restore_string():
    assert restore_string('q3w3e3rty') == "qqqwwweeerty"
    assert restore_string('qw2e3r4t5y') == "qwweeerrrrttttty"
    assert restore_string('g3h3t3r3qwerty') == "ggghhhtttrrrqwerty"
    assert restore_string('gn10b15') == "gnnnnnnnnnnbbbbbbbbbbbbbbb"
    assert restore_string('qwerty') == "qwerty"

