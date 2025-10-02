import pytest

@pytest.mark.parametrize("arg", [1,2,3])
def test_maintain(arg):
    assert arg is not None