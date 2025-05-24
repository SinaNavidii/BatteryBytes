import argparse
from config import setup_user_config
from generate_digest import generate_and_send_digest

def main():
    parser = argparse.ArgumentParser(
        prog='batterybytes',
        description="BatteryBytes CLI - Battery research digest delivery"
    )
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # batterybytes init
    subparsers.add_parser('init', help='Set up your preferences and email')

    # batterybytes send
    subparsers.add_parser('send', help='Generate and email the digest')

    args = parser.parse_args()

    if args.command == 'init':
        setup_user_config()
    elif args.command == 'send':
        generate_and_send_digest()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
