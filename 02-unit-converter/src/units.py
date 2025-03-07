unit_dict: dict[str, dict[str, float]] = {
    "Area": {
        "square meter": 1,
        "square kilometer": 1e-6,
        "square centimeter": 1e4,
        "square millimeter": 1e6,
        "square mile": 3.861e-7,
        "square yard": 1.19599,
        "square foot": 10.7639,
        "square inch": 1550.0031,
        "hectare": 1e-4,
        "acre": 0.000247105
    },
    "Data Transfer Rate": {
        "bit per second": 1,
        "kilobit per second": 1e-3,
        "megabit per second": 1e-6,
        "gigabit per second": 1e-9,
        "terabit per second": 1e-12,
        "byte per second": 1 / 8,
        "kilobyte per second": 1.25e-4,
        "megabyte per second": 1.25e-7,
        "gigabyte per second": 1.25e-10
    },
    "Digital Storage": {
        "bit": 1,
        "byte": 8,
        "kilobit": 1e3,
        "kilobyte": 8e3,
        "megabit": 1e6,
        "megabyte": 8e6,
        "gigabit": 1e9,
        "gigabyte": 8e9,
        "terabit": 1e12,
        "terabyte": 8e12
    },
    "Energy": {
        "joule": 1,
        "kilojoule": 1e-3,
        "calorie": 0.239006,
        "kilocalorie": 0.000239006,
        "watt-hour": 0.000277778,
        "kilowatt-hour": 2.7778e-7
    },
    "Frequency": {
        "hertz": 1,
        "kilohertz": 1e-3,
        "megahertz": 1e-6,
        "gigahertz": 1e-9
    },
    "Fuel Economy": {
        "kilometers per liter": 1,
        "miles per gallon": 2.35215,
        "liters per 100 kilometers": 100
    },
    "Length": {
        "meter": 1,
        "kilometer": 1e-3,
        "centimeter": 1e2,
        "millimeter": 1e3,
        "micrometer": 1e6,
        "nanometer": 1e9,
        "mile": 0.000621371,
        "yard": 1.09361,
        "foot": 3.28084,
        "inch": 39.3701
    },
    "Mass": {
        "kilogram": 1,
        "gram": 1e3,
        "milligram": 1e6,
        "metric ton": 1e-3,
        "long ton": 0.000984207,
        "short ton": 0.00110231,
        "pound": 2.20462,
        "ounce": 35.274
    },
    "Plane Angle": {
        "degree": 1,
        "radian": 0.0174533,
        "gradian": 1.11111
    },
    "Pressure": {
        "pascal": 1,
        "kilopascal": 1e-3,
        "megapascal": 1e-6,
        "bar": 1e-5,
        "psi": 0.000145038
    },
    "Speed": {
        "meter per second": 1,
        "kilometer per hour": 3.6,
        "mile per hour": 2.23694,
        "knot": 1.94384
    },
    "Temperature": {
        "celsius": 1,
        "fahrenheit": 1.8,
        "kelvin": 1
    },
    "Time": {
        "second": 1,
        "minute": 1 / 60,
        "hour": 1 / 3600,
        "day": 1 / 86400,
        "week": 1 / 604800,
        "month": 1 / 2.628e6,
        "year": 1 / 3.154e7
    },
    "Volume": {
        "liter": 1,
        "milliliter": 1e3,
        "cubic meter": 1e-3,
        "cubic centimeter": 1e3,
        "cubic millimeter": 1e6,
        "cubic inch": 61.0237,
        "cubic foot": 0.0353147,
        "cubic yard": 0.00130795
    }
}



def unit_converter(value: float, from_unit: str, to_unit: str, category: str):
    
    if category.lower() == "temperature":
        return temp_converter(value, from_unit, to_unit)

    from_unit_value = unit_dict[category][from_unit.lower()]
    to_unit_value = unit_dict[category][to_unit.lower()]

    result =  (to_unit_value / from_unit_value) * value
    return round(result, 2)



def temp_converter(value: float, from_unit: str, to_unit: str):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    converted_value = 0

    if from_unit == to_unit:
        converted_value = value

    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        converted_value = (value * 9/5) + 32

    if from_unit == 'fahrenheit' and to_unit == 'celsius':
        converted_value = (value - 32) * 5/9

    if from_unit == 'celsius' and to_unit == 'kelvin':
        converted_value = value + 273.15

    if from_unit == 'fahrenheit' and to_unit == 'kelvin':
        converted_value = (value - 32) * 5/9 + 273.15

    if from_unit == 'kelvin' and to_unit == 'celsius':
        converted_value = value - 273.15

    if from_unit == 'kelvin' and to_unit == 'fahrenheit':
        converted_value = (value - 273.15) * 9/5 + 32

    return round(converted_value, 2)


