def celsius_far(temp: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return temp * 9 / 5 + 32

def celsius_kelvin(temp: float) -> float:
    """Convert Celsius to Kelvin."""
    return temp + 273.15

print("what is the temperature in Celsius?")
temp = float(input())
print("Temperature in Fahrenheit:", celsius_far(temp))
print("Temperature in Kelvin:", celsius_kelvin(temp))