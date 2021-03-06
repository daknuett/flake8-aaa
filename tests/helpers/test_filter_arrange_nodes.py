import pytest

from flake8_aaa.helpers import filter_arrange_nodes


@pytest.mark.parametrize(
    'code_str', [
        '''
# Hello and welcome to a filter test

def test() -> None:  # line 4
    """
    This is a docstring
    """

    x = 1
    y = 2

    # This is a comment. line 12

    result = x + y  # line 14

    assert result == 3

'''
    ]
)
def test(first_node_with_tokens):
    result = filter_arrange_nodes(first_node_with_tokens.body, 14)

    assert len(result) == 2
    assert 'x = 1' in result[0].first_token.line
    assert 'y = 2' in result[1].first_token.line
