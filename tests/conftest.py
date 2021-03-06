import ast

import asttokens
import pytest
from flake8.defaults import MAX_LINE_LENGTH
from flake8.processor import FileProcessor


class FakeOptions:
    pass


@pytest.fixture
def fake_options():
    """
    Returns:
        FakeOptions
    """
    options = FakeOptions()
    options.hang_closing = False
    options.max_line_length = MAX_LINE_LENGTH
    options.max_doc_length = MAX_LINE_LENGTH
    options.verbose = False
    return options


@pytest.fixture
def file_tokens(code_str, tmpdir, fake_options):
    """
    Args:
        code_str (str): Code to be tokenized.

    Returns:
        list: List contains instances of ``tokenize.TokenInfo`` on Python3.
        This is to emulate the behaviour of ``FileProcessor`` which is using
        ``tokenize.generate_tokens``.
    """
    code_file = tmpdir.join('code_file.py')
    code_file.write(code_str)
    file_processor = FileProcessor(str(code_file), options=fake_options)
    tokens = file_processor.generate_tokens()
    return list(tokens)


@pytest.fixture
def first_token(file_tokens):
    """
    Args:
        file_tokens (list)

    Returns:
        First token of provided list.
    """
    return file_tokens[0]


@pytest.fixture
def first_node_with_tokens(code_str):
    """
    Given ``code_str`` fixture, parse that string with ``ast.parse`` and then
    augment it with ``asttokens.ASTTokens``.

    Returns:
        ast.node: First node in parsed tree.
    """
    tree = ast.parse(code_str)
    asttokens.ASTTokens(code_str, tree=tree)
    return tree.body[0]


@pytest.fixture
def lines(code_str):
    """
    Given ``code_str`` chop it into lines as flake8 would pass to a plugin.

    Returns:
        list (str)
    """
    return ['{}\n'.format(line) for line in code_str.split('\n')]
