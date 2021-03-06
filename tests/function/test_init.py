import pytest

from flake8_aaa.function import Function
from flake8_aaa.types import LineType


@pytest.mark.parametrize('code_str', ['''

def test():
    pass

def test_other():
    pass

# All done :D
'''])
def test(first_node_with_tokens, lines):
    result = Function(first_node_with_tokens, lines)

    assert result.node == first_node_with_tokens
    assert result.lines == [
        'def test():\n',
        '    pass\n',
    ]
    assert result.act_node is None
    assert result.line_markers == [LineType.unprocessed, LineType.unprocessed]
    assert result.line_markers.fn_offset == 3
    assert result.first_line_no == 3
