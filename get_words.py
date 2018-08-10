import os
import sys
import collections

import ast

from utilities.cli import CommandLineInterface
from utilities.parser import FolderParser, WebParser
from utilities.logger import Logger



def main():
    cli = CommandLineInterface(sys.argv)

    source_type = cli.get_source_type()
    part_of_speech = cli.get_part_of_speech()
    words_count = cli.get_words_count()

    if source_type == 'folder':
        parser = FolderParser(part_of_speech, words_count)
    elif source_type == 'web':
        parser = WebParser(part_of_speech, words_count)
    most_common_words = parser.parse_most_common_words(part_of_speech, words_count, directories=['target_folder'])
    Logger().message(debug_message=most_common_words)


if __name__== "__main__":
    main()
