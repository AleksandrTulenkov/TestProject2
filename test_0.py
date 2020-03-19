"""Command-line parsing program testing module."""
import parse_ver03


class Args():
    """Base class that provides test args creation"""

    def __init__(self, reverse, uppercase, text):
        self.reverse = reverse
        self.uppercase = uppercase
        self.text = text


def test_reverse_str():
    """Reverse test function."""
    assert parse_ver03.reverse_str('test input') == 'tupni tset'
    assert parse_ver03.reverse_str('test') == 'tset'
    assert parse_ver03.reverse_str('') == ''


def test_uppercase_str():
    """Uppercase test function."""
    assert parse_ver03.uppercase_str('test input') == 'TEST INPUT'
    assert parse_ver03.uppercase_str('test') == 'TEST'
    assert parse_ver03.uppercase_str('') == ''


def test_process_str():
    """Output process test function."""
    args = Args(True, False, 'test input')
    assert parse_ver03.process_str(args) == f'Reversed text: tupni tset'

    args = Args(False, True, 'test input')
    assert parse_ver03.process_str(args) == f'Uppercased text: TEST INPUT'

    args = Args(True, True, 'test input')
    assert parse_ver03.process_str(args) == 'Uppercased and ' + \
                                            'reversed text: TUPNI TSET'
