#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "hpost2019"


import sys
import argparse


def text_upper(text):
    return text.upper()


def text_lower(text):
    return text.lower()


def text_title(text):
    return text.title()


def create_parser():
    """Creates and returns an argparse cmd line option parser."""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        "-t", "--title", help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    """Implementation of echo."""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_help()
        exit(1)
    text = ns.text
    if ns.upper:
        text = text_upper(text)
    if ns.lower:
        text = text_lower(text)
    if ns.title:
        text = text_title(text)
    print(text)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
