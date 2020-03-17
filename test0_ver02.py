import argparse

def reverse_str(input_string):
    '''reverse text function'''
    return input_string[::-1]

def uppercase_str(input_string):
    '''uppercase text function'''
    return input_string.upper()

def main():
    parser = argparse.ArgumentParser(description='Reverse and uppercase text program')
    parser.add_argument("text", help="textline", type=str)
    parser.add_argument('-r', '--reverse', help='reverse flag', action="store_true")
    parser.add_argument('-u', '--uppercase', help='uppercase flag', action="store_true")
    parser.add_argument('-ru', '--revupp', help='reverse and uppercase flag', action="store_true")
    args = parser.parse_args()

    if args.reverse:
        print(reverse_str(args.text))
    elif args.uppercase:
        print(uppercase_str(args.text))
    elif args.revupp:
        print(reverse_str(uppercase_str(args.text)))

if __name__ == '__main__':
    main()
    