"""Command-line parsing program testing module."""
from collections import namedtuple
import reverse_uppercase


def test_reverse_str():
    """Reverse test function."""
    assert reverse_uppercase.reverse_str('test input') == 'tupni tset'
    assert reverse_uppercase.reverse_str('test') == 'tset'
    assert reverse_uppercase.reverse_str('') == ''


def test_uppercase_str():
    """Uppercase test function."""
    assert reverse_uppercase.uppercase_str('test input') == 'TEST INPUT'
    assert reverse_uppercase.uppercase_str('test') == 'TEST'
    assert reverse_uppercase.uppercase_str('') == ''


def test_process_str():
    """Output process test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['reverse', 'uppercase', 'text'])

    rev_input = Args(True, False, 'test input')
    assert reverse_uppercase.process_str(rev_input) == \
        (reverse_uppercase.REVERSE_LABEL, 'tupni tset')

    upper_input = Args(False, True, 'test input')
    assert reverse_uppercase.process_str(upper_input) == \
        (reverse_uppercase.UPPERCASE_LABEL, 'TEST INPUT')

    upper_rev_input = Args(True, True, 'test input')
    assert reverse_uppercase.process_str(upper_rev_input) == \
        (reverse_uppercase.UPPERCASE_AND_REVERSE_LABEL, 'TUPNI TSET')

    none_flags_input = Args(False, False, 'test input')
    assert reverse_uppercase.process_str(none_flags_input) is None

    none_input = Args(False, False, '')
    assert reverse_uppercase.process_str(none_input) is None
