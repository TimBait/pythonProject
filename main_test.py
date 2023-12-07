import pytest
from main import archive_string, restore_string, archive_string_isalpha, restore_string_isalnum

def test_archive_string():
    assert archive_string('qqqwwweeerty') == "q3w3e3rty"
    assert archive_string('qwweeerrrrttttty') == "qw2e3r4t5y"
    assert archive_string('ggghhhtttrrrqwerty') == "g3h3t3r3qwerty"
    assert archive_string('gnnnnnnnnnnbbbbbbbbbbbbbbb') == "gn10b15"
    assert archive_string('qwertyyy') != "q1w1e1r1t1y3"

def test_restore_string():
    assert restore_string('q3w3e3rty') == "qqqwwweeerty"
    assert restore_string('qw2e3r4t5y') == "qwweeerrrrttttty"
    assert restore_string('g3h3t3r3qwerty') == "ggghhhtttrrrqwerty"
    assert restore_string('gn10b15') == "gnnnnnnnnnnbbbbbbbbbbbbbbb"
    assert restore_string('qwerty') == "qwerty"

def test_archive_string_isalpha():
    assert archive_string_isalpha('qqqwwweeerty') == True
    assert archive_string_isalpha('qwweeerrrrttttty') == True
    assert archive_string_isalpha('ggghhhtttrrrqwerty') == True
    assert archive_string_isalpha('gnnnnnnnnnnbbbbbbbbbbbbbbb') == True
    assert archive_string_isalpha('qwertyyy') == True

    assert archive_string_isalpha('1qqqwwweeerty') == False
    assert archive_string_isalpha('q1w2e3r4t5') == False
    assert archive_string_isalpha('!!!qwerty!!!') == False
    assert archive_string_isalpha('!@#$$&&%') == False
    assert archive_string_isalpha('1000500qwerty') == False


def test_restore_string_isalnum():
    assert restore_string_isalnum('q3w3e3rty') == True
    assert restore_string_isalnum('qw2e3r4t5y') == True
    assert restore_string_isalnum('g3h3t3r3qwerty') == True
    assert restore_string_isalnum('gn10b15') == True
    assert restore_string_isalnum('q1w1e1r1t1y3') == True

    assert restore_string_isalnum('!!!qwerty!!!') == False
    assert restore_string_isalnum('!"№;%:%;№"!"') == False
    assert restore_string_isalnum('123asgd') == False
    assert restore_string_isalnum('1233425') == False
    assert restore_string_isalnum('1d2f4g5!!#$') == False
