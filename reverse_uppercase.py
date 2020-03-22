"""Command-line parsing program."""
import argparse

UPPERCASE_LABEL = 'Uppercased text:'
REVERSE_LABEL = 'Reversed text:'
UPPERCASE_AND_REVERSE_LABEL = 'Uppercase and reverse text:'


def reverse_str(input_string):
    """Reverse text function."""
    return input_string[::-1]


def uppercase_str(input_string):
    """Uppercase text function."""
    return input_string.upper()


def parse_args():
    """Parse args text function."""
    parser = argparse.ArgumentParser(
        description='Reverse and uppercase text program')
    parser.add_argument('text',
                        help='textline', type=str)
    parser.add_argument('-r', '--reverse',
                        help='reverse flag', action='store_true')
    parser.add_argument('-u', '--uppercase',
                        help='uppercase flag', action='store_true')
    args = parser.parse_args()
    if not args.reverse and not args.uppercase:
        parser.print_help()
    return args


def process_str(args):
    """Output process function."""
    if args.reverse and args.uppercase:
        output = reverse_str(uppercase_str(args.text))
        return UPPERCASE_AND_REVERSE_LABEL, output
    elif args.reverse:
        output = reverse_str(args.text)
        return REVERSE_LABEL, output
    elif args.uppercase:
        output = uppercase_str(args.text)
        return UPPERCASE_LABEL, output
    else:
        return None


def main():
    """Realization of main function."""
    args = parse_args()
    if process_str(args) is not None:
        label, output = process_str(args)
        print(label, output)


if __name__ == '__main__':
    main()
