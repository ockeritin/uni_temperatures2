from temperature import celsius_to_fahrenheit, classify_temperature


def test_freezing_point_conversion():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point_conversion():
    assert celsius_to_fahrenheit(100) == 212


def test_classifies_freezing_temperature():
    assert classify_temperature(-2) == "freezing"


def test_classifies_mild_temperature():
    assert classify_temperature(18) == "mild"