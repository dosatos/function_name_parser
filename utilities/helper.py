import ast
import os
import logging

from nltk import pos_tag


class CommandLineInterfaceParser:

    def __init__(self, arguments):
        self.verify_cli(arguments)
        self.arguments = arguments
        self.command = self.parse_command(arguments)
        self.argument = self.parse_number_of_words(arguments)
        self.project_directories = self.parse_project_directories(arguments)

    def get_arguments(self):
        return self.arguments

    def parse_command(self, arguments):
        return arguments[1]

    def get_command(self):
        return self.command

    def parse_number_of_words(self):
        if self.command == 'parse':
            try:
                return int(arguments[2])
            except TypeError as e:
                raise TypeError(cli_error_message)

    def parse_project_directories(self):
        if self.command == 'parse':
            return arguments[3:]

    def verify_cli(self, arguments):
        available_actions = ['parse']
        if len(arguments) < 4 or arguments[2] not in available_actions:
            raise AttributeError(cli_error_message)
    
    def get_words_limit(self):
        return sys.argv[1]

    def get_words_limit(self):
        return sys.argv[1]

    def get_directories(self):
        return sys.argv[2:]


def transform_to_list(trees):
    list_of_trees = []
    for tree in trees:
        lower_cased_function = [node.name.lower()
                                for node in ast.walk(tree)
                                    if isinstance(node, ast.FunctionDef)]
        list_of_trees.append(lower_cased_function)
    return flatten(list_of_trees)


def is_special_function(f):
    return f.startswith('__') and f.endswith('__')


def flatten(lst):
    return sum([list(item) for item in lst], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return 'VB' in pos_info[0][1]


def custom_file_path_filter(files, dirname, extension=".py"):
    return [os.path.join(dirname, f)
                for f in files if f.endswith(extension)]


def log_to_file(debug_message):
    logging.basicConfig(filename='frequently_used_verbs.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')
    logging.debug(debug_message)


def log_error(debug_message):
    logging.basicConfig(filename='errors.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')
    logging.debug(debug_message)


cli_error_message = """ 
Please, to run the program use the following structure:

python3 verbs.py <source_type> <number_of_words>

For example,
>>> python3 get_func_words.py <count> <POS> <source>

:count  int: number of words
:POS    str: (part of speach). Choose from verb VB, noun NN
:source str: source of words. Choose from web, folder
""" 