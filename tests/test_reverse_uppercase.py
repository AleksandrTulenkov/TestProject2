"""Command-line parsing program testing module."""
from collections import namedtuple
from module import reverse_uppercase


def test_reverse_str():
    """Reverse text test function."""
    assert reverse_uppercase.reverse_str('test input') == 'tupni tset'
    assert reverse_uppercase.reverse_str('test') == 'tset'


def test_reverse_empty():
    """Reverse empty text test function."""
    assert reverse_uppercase.reverse_str('') == ''


def test_uppercase_str():
    """Uppercase text test function."""
    assert reverse_uppercase.uppercase_str('test input') == 'TEST INPUT'
    assert reverse_uppercase.uppercase_str('test') == 'TEST'


def test_uppercase_empty():
    """Uppercase empty text test function."""
    assert reverse_uppercase.uppercase_str('') == ''


def test_process_reverse():
    """Output process reverse test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['reverse', 'uppercase', 'text'])

    rev_input = Args(True, False, 'test input')
    assert reverse_uppercase.process_str(rev_input) == \
        (reverse_uppercase._REVERSE_LABEL, 'tupni tset')


def test_process_uppercase():
    """Output process uppercase test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['reverse', 'uppercase', 'text'])
    upper_input = Args(False, True, 'test input')
    assert reverse_uppercase.process_str(upper_input) == \
        (reverse_uppercase._UPPERCASE_LABEL, 'TEST INPUT')


def test_process_both():
    """Output process uppercase and reverse test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['reverse', 'uppercase', 'text'])
    upper_rev_input = Args(True, True, 'test input')
    assert reverse_uppercase.process_str(upper_rev_input) == \
        (reverse_uppercase._UPPERCASE_AND_REVERSE_LABEL, 'TUPNI TSET')


def test_process_none_flags():
    """Output process uppercase and reverse without flags test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['reverse', 'uppercase', 'text'])
    none_flags_input = Args(False, False, 'test input')
    assert reverse_uppercase.process_str(none_flags_input) is None


def test_process_none_text():
    """Output process uppercase and reverse without text test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['reverse', 'uppercase', 'text'])
    none_input = Args(False, False, '')
    assert reverse_uppercase.process_str(none_input) is None
