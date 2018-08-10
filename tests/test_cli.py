import pytest
from ..utilities.cli import CommandLineInterface


@pytest.fixture
def cli():
	return CommandLineInterface
	

def test_all_arguments_correct(cli):
	cli(['python', 'web', 'verb', '10'])
		

def test_source_type_wrong(cli):
	with pytest.raises(AttributeError):
		cli(['python', 'fold', 'verb', '10'])


def test_pos_wrong(cli):
	with pytest.raises(AttributeError):
		cli(['python', 'folder', 'Verb', '10'])


def test_word_count_wrong(cli):
	with pytest.raises(ValueError):
		cli(['python', 'folder', 'verb', 'ten'])