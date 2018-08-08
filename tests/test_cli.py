import pytest
from hw2.utilities.cli import CommandLineInterface


@pytest.fixture
def cli():
	return CommandLineInterface
	

def test_all_arguments_correct(cli):
	with pytest.raises(TypeError):
		cli(['python', 'web', '10', 'VB'])


def test_source_type_wrong(cli):
	with pytest.raises(TypeError):
		cli(['python', 'fold', '10', 'VB'])


def test_word_count_wrong(cli):
	with pytest.raises(TypeError):
		cli(['python', 'folder', 'ten', 'VB'])


def test_pos_wrong(cli):
	with pytest.raises(TypeError):
		cli(['python', 'folder', '10', 'Vb'])