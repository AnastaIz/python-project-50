#!/usr/bin/env python3
from gendiff.cli import parse_args_cli


def main():
    args = parse_args_cli()
    print(args)


if __name__ == '__main__':
    main()
