from .exceptions import NotActionBlock
from .helpers import node_is_pytest_raises, node_is_result_assignment
from .types import ActBlockType


class ActBlock(object):
    """
    Attributes:
        node
        block_type (ActBlockType)
    """

    def __init__(self, node, block_type):
        """
        Args:
            node
            block_type (ActBlockType)
        """
        self.node = node
        self.block_type = block_type

    @classmethod
    def build(cls, node):
        """
        Args:
            node (ast.node): A node, decorated with ``ASTTokens``.

        Returns:
            ActBlock

        Raises:
            NotActionBlock: When ``node`` does not look like an Act block.
        """
        if node_is_result_assignment(node):
            return cls(node, ActBlockType.result_assignment)
        elif node_is_pytest_raises(node):
            return cls(node, ActBlockType.pytest_raises)

        # Check if line marked with '# act'
        if node.first_token.line.strip().endswith('# act'):
            return cls(node, ActBlockType.marked_act)

        raise NotActionBlock()
