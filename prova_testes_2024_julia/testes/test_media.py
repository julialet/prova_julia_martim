import pytest
from stat_funcs import StatsN2

@pytest.mark.media
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 3.0),
    ([1, 1, 1, 1, 1], 1.0),
    ([1, 2, 2, 2, 5], 2.4),
])
def test_media(lista, expected):
    assert StatsN2.media(lista) == expected

@pytest.mark.media
@pytest.mark.xfail
def test_media_fail():
    assert StatsN2.media([]) == 1.0
