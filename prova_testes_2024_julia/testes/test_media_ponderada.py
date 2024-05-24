# testes/test_media_ponderada.py
import pytest
from stat_funcs import StatsN2

@pytest.mark.media_ponderada
@pytest.mark.parametrize("lista, pesos, expected", [
    ([1, 2, 3, 4, 5], [0.1, 0.2, 0.3, 0.4, 0.5], 3.6666666666666665),
    ([1, 2, 3, 4], [1, 1, 1, 1], 2.5),
])
def test_media_ponderada_param(lista, pesos, expected):
    assert StatsN2.media_ponderada(lista, pesos) == expected

@pytest.mark.media_ponderada
@pytest.mark.xfail
def test_media_ponderada_fail():
    assert StatsN2.media_ponderada([], []) == 1.0

