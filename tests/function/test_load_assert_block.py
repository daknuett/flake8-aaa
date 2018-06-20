import pytest

from flake8_aaa.assert_block import AssertBlock


@pytest.mark.parametrize(
    'code_str', ['''
def test():
    with pytest.raises(DoesNotExist):
        load_account(-1)
''']
)
def test_none(function_with_act_block):
    result = function_with_act_block.load_assert_block()

    assert result is None


@pytest.mark.parametrize(
    'code_str', [
        '''
def test():
    result = load_account(1)

    assert isinstance(result, Account)
    assert result.id == 1
''',
        '''
def test_raise(toy_instance):
    with pytest.raises(PlayError) as excinfo:
        toy_instance.run()

    assert 'Not ready' in excinfo.value.message
    assert toy_instance.has_run is False
''',
    ]
)
def test(function_with_act_block):
    result = function_with_act_block.load_assert_block()

    assert isinstance(result, AssertBlock)
    assert len(result.nodes) == 2
