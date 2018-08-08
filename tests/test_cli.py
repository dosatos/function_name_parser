import pytest
from hw2.utilities import cli


@pytest.fixture
def clip():
	return cli.CommandLineInterfaceParser
	

def test_all_arguments_correct(clip):
	with pytest.raises(TypeError):
		cli = clip(['python', 'web', '10', 'VB'])


def test_source_type_wrong(clip):
	with pytest.raises(TypeError):
		cli = clip(['python', 'fold', '10', 'VB'])


def test_word_count_wrong(clip):
	with pytest.raises(TypeError):
		cli = clip(['python', 'folder', 'ten', 'VB'])


def test_pos_wrong(clip):
	with pytest.raises(TypeError):
		cli = clip(['python', 'folder', '10', 'Vb'])