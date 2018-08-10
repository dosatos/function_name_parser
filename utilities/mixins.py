import ast
from nltk import pos_tag
# from logger import Logger


class ValidatorMixin:

    def __init__(self):
        self.error_message = """ 

========================================================================
    To run the program use the following format, please:
    
    >>> python3 get_words.py <source_type> <POS> <words_count>
        

        :source_type      str: source type. Available: [web, folder]
        :POS         str: (part of speech). Available: [verb, noun]
        :words_count  int: number of words
        

    For example:

    >>> python3 get_words.py folder verb 105

    OR

    >>> python3 get_words.py web noun 77
        
========================================================================

    """
        self.parts_of_speech = ['verb', 'noun']
        self.source_types = ['folder', 'web']


    def validate_source_type(self, source_type):
        if source_type not in self.source_types:
            raise AttributeError("Wrong source type.\n", self.error_message)
    
    def validate_part_of_speech(self, part_of_speech):
        if part_of_speech not in self.parts_of_speech:
            raise AttributeError(f"not supported part of speech \n {self.error_message}")

    def validate_words_count(self, words_count):
        try:
            return int(words_count)
        except ValueError as e:
            raise ValueError("Wrong word count.\n", self.error_message)

    def validate_most_common_words(self, counter):
    	if not isinstance(counter, dict):
    		raise TypeError("Wrong word counter format")


class PyScriptParserMixin:

    def get_trees(self, paths):
        for path in paths:
            content = self.get_content(path)
            yield ast.parse(content)

    def parse_functions(self, tree):
        return [node.name.lower() 
                for node in ast.walk(tree) 
                if isinstance(node, ast.FunctionDef)]

    def parse_words_of_given_pos(self, func_names, pos):
        look_up_tag = self.get_look_up_tag(pos)
        words = []
        for func_name in func_names:
            if self.is_special_function(func_name):
                continue
            words.extend([word for word in func_name.split('_') if word])
        return [word for word, tag in pos_tag(words) if look_up_tag in tag]

    def get_look_up_tag(self, pos):
        look_up_tags = {'verb': 'VB', 'noun': 'NN'}
        return look_up_tags[pos]

    def is_special_function(self, f):
        return f.startswith('__') and f.endswith('__')