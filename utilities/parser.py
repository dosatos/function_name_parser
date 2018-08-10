import os
import collections

from .mixins import ValidatorMixin, PyScriptParserMixin


class Parser(ValidatorMixin, PyScriptParserMixin):
    def __init__(self, part_of_speech, words_count):
        super().__init__()
        self.script_files = []
        self.part_of_speech = None
        self.words_count = None
        self.most_common_words = collections.Counter()

        self.set_part_of_speech(part_of_speech)
        self.set_words_count(words_count)

    def get_script_files(self):
        return self.files

    def set_script_files(self, files):
        self.files = files

    def get_part_of_speech(self):
        return self.part_of_speech

    def set_part_of_speech(self, part_of_speech):
        self.validate_part_of_speech(part_of_speech)
        self.part_of_speech = part_of_speech

    def get_words_count(self):
        return self.words_count

    def set_words_count(self, words_count):
        self.validate_words_count(words_count)
        self.words_count = words_count

    def get_most_common_words(self):
        return self.most_common_words

    def set_most_common_words(self, counter):
        self.most_common_words = counter

    def get_words(self, paths, pos):
        content_holding_trees = self.get_trees(paths)
        func_names = []
        for tree in content_holding_trees:
            func_names.extend(self.parse_functions(tree))
        return self.parse_words_of_given_pos(func_names, pos)


class FolderParser(Parser):

    def __init__(self, part_of_speech, words_count):
        super().__init__(part_of_speech, words_count)

    def parse_folder(self, part_of_speech, words_count, directories):
        paths = self.get_paths_to_script_files(directories)
        words = self.get_words(paths, part_of_speech)
        most_common_words = collections.Counter(words).most_common(words_count)
        return most_common_words

    def get_paths_to_script_files(self, directories, extension=".py"):
        paths = []
        for directory in directories:
            for dirname, _, filenames in os.walk(directory, topdown=True):
                paths.extend([os.path.join(dirname, filename) 
                              for filename in filenames if filename.endswith(extension)])
        return paths

    def get_content(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content


class WebParser(Parser):
	pass
