import pytest
from stat_funcs import StatsN2

@pytest.mark.multimodal
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 2, 3, 3, 4], [2, 3]),
    ([1, 1, 2, 3, 4], "Não é multimodal"),
])
def test_multimodal(lista, expected):
    assert StatsN2.multimodal(lista) == expected

@pytest.mark.multimodal
@pytest.mark.xfail
def test_multimodal_fail():
    assert StatsN2.multimodal([]) == 1
