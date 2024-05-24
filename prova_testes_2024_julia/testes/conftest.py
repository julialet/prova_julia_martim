import pytest

@pytest.fixture
def sample_data():
    return {
        "numeros_unimodal": [1, 2, 2, 3, 4],
        "numeros_multimodal": [1, 2, 2, 3, 3, 4],
        "numeros_amodal": [1, 2, 3, 4, 5],
        "pesos": [0.1, 0.2, 0.3, 0.4, 0.5]
    }
