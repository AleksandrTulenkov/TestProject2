"""Command-line parsing program."""
import argparse


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
    parser.add_argument("text",
                        help="textline", type=str)
    parser.add_argument('-r', '--reverse',
                        help='reverse flag', action="store_true")
    parser.add_argument('-u', '--uppercase',
                        help='uppercase flag', action="store_true")

    args = parser.parse_args()
    return args


def process_str(args):
    """Output process function."""
    if args.reverse and args.uppercase:
        output = 'Uppercased and reversed text: ' + \
                f'{reverse_str(uppercase_str(args.text))}'
    elif args.reverse:
        output = f'Reversed text: {reverse_str(args.text)}'
    elif args.uppercase:
        output = f'Uppercased text: {uppercase_str(args.text)}'
    return output


def main():
    """Realization of main function."""
    args = parse_args()
    print(process_str(args))


if __name__ == '__main__':
    main()
