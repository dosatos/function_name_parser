import os
import sys
import collections

import ast

from utilities.cli import CommandLineInterface
from utilities.parser import Parser


def main():
    cli = CommandLineInterface(sys.argv)

    source_type = cli.get_source_type()
    part_of_speach = cli.get_part_of_speach()
    words_count = cli.get_words_count()

    parser = Parser()
    if source_type == 'folder':
        parser.parse_folder(part_of_speach, words_count)
    elif source_type == 'web':
        parser.parse_url(part_of_speach, words_count)


if __name__== "__main__":
    main()
