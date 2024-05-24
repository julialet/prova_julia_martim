import pytest
from stat_funcs import StatsN2

@pytest.mark.dpadrao
@pytest.mark.parametrize("var, expected", [
    (4, 2),
    (9, 3),
    (16, 4),
])
def test_dpadrao(var, expected):
    assert StatsN2.dpadrao(var) == expected

@pytest.mark.dpadrao
@pytest.mark.xfail
def test_dpadrao_fail():
    assert StatsN2.dpadrao(0) == 1.0
