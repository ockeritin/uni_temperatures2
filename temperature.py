def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def classify_temperature(celsius):
    if celsius < 0:
        return "freezing"
    elif celsius < 20:
        return "mild"
    else:
        return "hot"