import pytest
from stat_funcs import StatsN2

@pytest.mark.skew
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 2, 3, 3, 4], "Distribuição normal"),
    ([1, 1, 1, 1, 1], "Distribuição negativa"),
])
@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_skew(lista, expected):
    assert StatsN2.skew(lista) == expected

@pytest.mark.skew
@pytest.mark.xfail
@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_skew_fail():
    assert StatsN2.skew([]) == "Distribuição normal"
