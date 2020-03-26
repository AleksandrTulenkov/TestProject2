"""Command-line parsing program."""
import argparse
from sys import exit

_UPPERCASE_LABEL = 'Uppercased text:'
_REVERSE_LABEL = 'Reversed text:'
_UPPERCASE_AND_REVERSE_LABEL = 'Uppercase and reverse text:'


def reverse_str(input_string):
    """Reverse text function."""
    return input_string[::-1]


def uppercase_str(input_string):
    """Uppercase text function."""
    return input_string.upper()


def read_input_file(input_filename):
    """Read input text from file function."""
    try:
        with open(input_filename, 'r') as file:
            text = file.read().replace('\n', '')
            return text
    except IOError as err:
        print("Could not read file:{0.filename}".format(err))
        exit()


def write_output_file(output_filename, label, text):
    """Write result text to output file function."""
    with open(output_filename, 'w') as file:
        return file.write(label+text)


def parse_args():
    """Parse args text function."""
    parser = argparse.ArgumentParser(
        description='Reverse and uppercase text program')
    parser.add_argument('filename',
                        help='filename with input text', type=str)
    parser.add_argument('-r', '--reverse',
                        help='reverse flag', action='store_true')
    parser.add_argument('-u', '--uppercase',
                        help='uppercase flag', action='store_true')
    parser.add_argument('-f', '--file_output',
                        help='save results into file "output_filename"',
                        action='store_true')
    args = parser.parse_args()
    if not args.reverse and not args.uppercase:
        parser.print_help()
    return args


def process_str(args, text):
    """Output process function."""
    if not args.reverse and not args.uppercase:
        return None
    elif not text:
        print(f'{args.filename} is empty')
        return None
    else:
        params_dict = {'filename': args.filename,
                       'file_output': args.file_output,
                       'label': '',
                       'text_output': ''}

        if args.reverse and args.uppercase:
            params_dict['text_output'] = reverse_str(uppercase_str(text))
            params_dict['label'] = _UPPERCASE_AND_REVERSE_LABEL

        elif args.reverse:
            params_dict['text_output'] = reverse_str(text)
            params_dict['label'] = _REVERSE_LABEL

        elif args.uppercase:
            params_dict['text_output'] = uppercase_str(text)
            params_dict['label'] = _UPPERCASE_LABEL

        return params_dict


def main():
    """Realization of main function."""
    args = parse_args()
    text = read_input_file(args.filename)
    params = process_str(args, text)
    if params is not None:
        if params['file_output']:
            output_filename = 'output_'+params['filename']
            write_output_file(output_filename,
                              params['label'],
                              params['text_output'])
            print(f'{output_filename} created')
        else:
            print(params['label'], params['text_output'])


if __name__ == '__main__':
    main()
