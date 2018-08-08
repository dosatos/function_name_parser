import pytest
from utilities import cli


@pytest.fixture
def setup():
	return cli.CommandLineInterfaceParser


def test_all_arguments_correct(setup):
	with pytest.raises(TypeError):
		cli = setup(['python', 'web', '10', 'VB'])


def test_source_type_wrong(setup):
	with pytest.raises(TypeError):
		cli = setup(['python', 'fold', '10', 'VB'])


def test_word_count_wrong(setup):
	with pytest.raises(TypeError):
		cli = setup(['python', 'folder', 'ten', 'VB'])


def test_pos_wrong(setup):
	with pytest.raises(TypeError):
		cli = setup(['python', 'folder', '10', 'Vb'])