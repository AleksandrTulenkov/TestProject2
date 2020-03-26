"""Command-line parsing program testing module."""
from collections import namedtuple
from boot_camp import reverse_uppercase


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
    Args = namedtuple('Args', ['filename',
                               'reverse',
                               'uppercase',
                               'file_output'])

    rev_input = Args('test.txt', True, False, False)
    text_input = 'test input'

    fuction_output = {'filename': 'test.txt',
                      'file_output': False,
                      'label': reverse_uppercase._REVERSE_LABEL,
                      'text_output': 'tupni tset'}

    assert reverse_uppercase.process_str(rev_input,
                                         text_input) == fuction_output


def test_process_uppercase():
    """Output process uppercase test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['filename',
                               'reverse',
                               'uppercase',
                               'file_output'])

    upper_input = Args('test.txt', False, True, False)
    text_input = 'test input'

    fuction_output = {'filename': 'test.txt',
                      'file_output': False,
                      'label': reverse_uppercase._UPPERCASE_LABEL,
                      'text_output': 'TEST INPUT'}

    assert reverse_uppercase.process_str(upper_input,
                                         text_input) == fuction_output


def test_process_both():
    """Output process uppercase and reverse test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['filename',
                               'reverse',
                               'uppercase',
                               'file_output'])

    upper_rev_input = Args('test.txt', True, True, False)
    text_input = 'test input'

    fuction_output = {'filename': 'test.txt',
                      'file_output': False,
                      'label': reverse_uppercase._UPPERCASE_AND_REVERSE_LABEL,
                      'text_output': 'TUPNI TSET'}

    assert reverse_uppercase.process_str(upper_rev_input,
                                         text_input) == fuction_output


def test_process_both_to_file():
    """Output into file process uppercase and reverse test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['filename',
                               'reverse',
                               'uppercase',
                               'file_output'])

    upper_rev_input = Args('test.txt', True, True, True)
    text_input = 'test input'

    fuction_output = {'filename': 'test.txt',
                      'file_output': True,
                      'label': reverse_uppercase._UPPERCASE_AND_REVERSE_LABEL,
                      'text_output': 'TUPNI TSET'}

    assert reverse_uppercase.process_str(upper_rev_input,
                                         text_input) == fuction_output


def test_process_none_flags():
    """Output process uppercase and reverse without flags test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['filename',
                               'reverse',
                               'uppercase',
                               'file_output'])

    none_flags_input = Args('test.txt', False, False, False)
    text_input = 'test input'

    assert reverse_uppercase.process_str(none_flags_input,
                                         text_input) is None


def test_process_none_text():
    """Output process uppercase and reverse without text test function."""
    # Namedtuple Args provides argparse args object
    Args = namedtuple('Args', ['filename',
                               'reverse',
                               'uppercase',
                               'file_output'])

    none_text_input = Args('test.txt', True, False, False)
    text_input = ''

    assert reverse_uppercase.process_str(none_text_input,
                                         text_input) is None


def test_write_output_file(tmpdir):
    file = tmpdir.join('test_write_func.txt')
    text = 'TEST INPUT'
    label = reverse_uppercase._UPPERCASE_LABEL
    reverse_uppercase.write_output_file(str(file), label, text)
    assert file.read() == label+text


def test_read_input_file(tmpdir):
    file = tmpdir.join('test_read_func.txt')
    text = 'test input'
    file.write(text)
    assert reverse_uppercase.read_input_file(str(file)) == text
