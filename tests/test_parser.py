import pytest

from ..utilities.parser import Parser, FolderParser


@pytest.fixture
def parser_setup():
	return Parser('verb', 10)


@pytest.fixture
def folder_parser_setup():
	return FolderParser('verb', 10)


@pytest.fixture
def folder_paths():
	return ['target_folder/file1.py', 'target_folder/file2.py']


def test_parser_init():
	word = 'verb'
	words_count = 10
	parser = Parser(word, words_count)
	assert parser.get_part_of_speech() == word and parser.get_words_count() == words_count


def test_parser_init_error():
	word = 'ver'
	words_count = 10
	with pytest.raises(AttributeError):
		parser = Parser(word, words_count)
		assert parser.get_part_of_speech() == word and parser.get_words_count() == words_count


def test_get_paths_to_script_files(folder_parser_setup):
	parser = folder_parser_setup
	directories = 'target_folder'
	filenames = parser.get_paths_to_script_files(directories)
	for filename in filenames:
		assert isinstance(filename, str)
		break


def test_folder_get_content(folder_parser_setup, folder_paths):
	path = folder_paths[0]
	content = folder_parser_setup.get_content(path)
	assert content.split('\n')[0] == "def get_values():"


def test_folder_get_words(folder_parser_setup, folder_paths):
	words = folder_parser_setup.get_words(folder_paths, 'verb')
	assert words == ['get', 'print', 'obtain', 'simplify', 'take', 'took', 'obtain']


def test_parse_folder(folder_parser_setup):
	directories = ['target_folder']
	most_common_words = folder_parser_setup.parse_most_common_words('verb', words_count=10, directories=directories)
	assert most_common_words == [('obtain', 2), ('print', 1), ('simplify', 1), ('take', 1), ('took', 1)]