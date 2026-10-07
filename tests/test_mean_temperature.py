import pytest

from temperature import mean_temperature


def test_mean_temperature():
    assert mean_temperature([10, 20, 30]) == 20


def test_mean_temperature_rejects_empty_list():
    with pytest.raises(ValueError):
        mean_temperature([])