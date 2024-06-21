#! /usr/bin/env python
"""
Say Hello to anyone, default Hello, World!
"""
import argparse


def get_args():
    """
    Get command line paragram
    """
    parser = argparse.ArgumentParser(description="Say Hello To Anyone")
    parser.add_argument("-n", "--name",
                        metavar="name",
                        default="World",
                        help="Type Your Name")
    return parser.parse_args()


def main():
    """
    The magic things happen.
    """
    args = get_args()
    print(f"Hello, {args.name}!")


if __name__ == '__main__':
    main()
