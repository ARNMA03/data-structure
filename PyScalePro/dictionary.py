# Dictionary containing conversion factors for storage units
storage_conversions = {
    "Bytes": {
        "Bytes": 1, "Kilobytes": 1e-3, "Megabytes": 1e-6,
        "Gigabytes": 1e-9, "Terabytes": 1e-12, "Petabytes": 1e-15
    },
    "Kilobytes": {
        "Bytes": 1e3, "Kilobytes": 1, "Megabytes": 1e-3,
        "Gigabytes": 1e-6, "Terabytes": 1e-9, "Petabytes": 1e-12
    },
    "Megabytes": {
        "Bytes": 1e6, "Kilobytes": 1e3, "Megabytes": 1,
        "Gigabytes": 1e-3, "Terabytes": 1e-6, "Petabytes": 1e-9
    },
    "Gigabytes": {
        "Bytes": 1e9, "Kilobytes": 1e6, "Megabytes": 1e3,
        "Gigabytes": 1, "Terabytes": 1e-3, "Petabytes": 1e-6
    },
    "Terabytes": {
        "Bytes": 1e12, "Kilobytes": 1e9, "Megabytes": 1e6,
        "Gigabytes": 1e3, "Terabytes": 1, "Petabytes": 1e-3
    },
    "Petabytes": {
        "Bytes": 1e15, "Kilobytes": 1e12, "Megabytes": 1e9,
        "Gigabytes": 1e6, "Terabytes": 1e3, "Petabytes": 1
    }
}
# Dictionary containing conversion factors for data speed units
data_speed_conversions = {
    "Kilobits": {
        "Kilobits": lambda x: x, "Megabits": lambda x: x * 1e-3, "Gigabits": lambda x: x * 1e-6
    },
    "Megabits": {
        "Kilobits": lambda x: x * 1e3, "Megabits": lambda x: x, "Gigabits": lambda x: x * 1e-3
    },
    "Gigabits": {
        "Kilobits": lambda x: x * 1e6, "Megabits": lambda x: x * 1e3, "Gigabits": lambda x: x
    }
}
# Dictionary containing conversion factors for length units
length_conversions = {
    "Kilometre": {
        "Kilometre": 1, "Metre": 1000, "Centimetre": 100000,
        "Millimetre": 1e+6, "Micrometre": 1e+9, "Mile": 0.621371,
        "Yard": 1094, "Foot": 3281, "Inch": 39370
    },
    "Metre": {
        "Kilometre": 0.001, "Metre": 1, "Centimetre": 100,
        "Millimetre": 1000, "Micrometre": 1e+6, "Mile": 0.000621371,
        "Yard": 1.094, "Foot": 3.281, "Inch": 39.37
    },
    "Centimetre": {
        "Kilometre": 1e-5, "Metre": 0.01, "Centimetre": 1,
        "Millimetre": 10, "Micrometre": 10000, "Mile": 6.2137e-6,
        "Yard": 0.01094, "Foot": 0.03281, "Inch": 0.3937
    },
    "Millimetre": {
        "Kilometre": 1e-6, "Metre": 0.001, "Centimetre": 0.1,
        "Millimetre": 1, "Micrometre": 1000, "Mile": 6.2137e-7,
        "Yard": 0.001094, "Foot": 0.003281, "Inch": 0.03937
    },
    "Micrometre": {
        "Kilometre": 1e-9, "Metre": 1e-6, "Centimetre": 0.0001,
        "Millimetre": 0.001, "Micrometre": 1, "Mile": 6.2137e-10,
        "Yard": 1.094e-6, "Foot": 3.281e-6, "Inch": 3.937e-5
    },
    "Mile": {
        "Kilometre": 1.60934, "Metre": 1609.34, "Centimetre": 160934,
        "Millimetre": 1.609e+6, "Micrometre": 1.609e+9, "Mile": 1,
        "Yard": 1760, "Foot": 5280, "Inch": 63360
    },
    "Yard": {
        "Kilometre": 0.0009144, "Metre": 0.9144, "Centimetre": 91.44,
        "Millimetre": 914.4, "Micrometre": 914400, "Mile": 0.000568182,
        "Yard": 1, "Foot": 3, "Inch": 36
    },
    "Foot": {
        "Kilometre": 0.0003048, "Metre": 0.3048, "Centimetre": 30.48,
        "Millimetre": 304.8, "Micrometre": 304800, "Mile": 0.000189394,
        "Yard": 0.333333, "Foot": 1, "Inch": 12
    },
    "Inch": {
        "Kilometre": 2.54e-5, "Metre": 0.0254, "Centimetre": 2.54,
        "Millimetre": 25.4, "Micrometre": 25400, "Mile": 1.5783e-5,
        "Yard": 0.0277778, "Foot": 0.0833333, "Inch": 1,
    }
}
# Dictionary containing conversion factors for mass units
mass_conversions = {
    "Kilogram": {
        "Kilogram": 1, "Gram": 1000,
        "Milligram": 1e+6, "Imperial ton": 0.000984207,
        "Pound": 2.20462, "Ounce": 35.274
    },
    "Gram": {
        "Kilogram": 0.001, "Gram": 1,
        "Milligram": 1000, "Imperial ton": 9.8421e-7,
        "Pound": 0.00220462, "Ounce": 0.035274
    },
    "Milligram": {
        "Kilogram": 1e-6, "Gram": 0.001,
        "Milligram": 1, "Imperial ton": 9.8421e-10,
        "Pound": 2.2046e-6, "Ounce": 3.5274e-5
    },
    "Imperial ton": {
        "Kilogram": 1016.05, "Gram": 1016050,
        "Milligram": 1.016e+9, "Imperial ton": 1,
        "Pound": 2240, "Ounce": 35840
    },
    "Pound": {
        "Kilogram": 0.453592, "Gram": 453.592,
        "Milligram": 453592, "Imperial ton": 0.000446429,
        "Pound": 1, "Ounce": 16
    },
    "Ounce": {
        "Kilogram": 0.0283495, "Gram": 28.3495,
        "Milligram": 28349.5, "Imperial ton": 2.7902e-5,
        "Pound": 0.0625, "Ounce": 1
    }
}
# Dictionary containing conversion factors for speed units
speed_conversions = {
    "Mile/hour": {
        "Mile/hour": 1, "Kilometer/hour": 1.60934,
        "Meter/second": 0.44704, "Knot": 0.868976,
        "Mach": 0.00293858
    },
    "Kilometer/hour": {
        "Mile/hour": 0.621371, "Kilometer/hour": 1,
        "Meter/second": 0.277778, "Knot": 0.539957,
        "Mach": 0.001823
    },
    "Meter/second": {
        "Mile/hour": 2.23694, "Kilometer/hour": 3.6,
        "Meter/second": 1, "Knot": 1.94384,
        "Mach": 0.006628
    },
    "Knot": {
        "Mile/hour": 1.15078, "Kilometer/hour": 1.852,
        "Meter/second": 0.514444, "Knot": 1,
        "Mach": 0.003384
    },
    "Mach": {
        "Mile/hour": 340.293, "Kilometer/hour": 1234.8,
        "Meter/second": 343.2, "Knot": 295.687,
        "Mach": 1
    }
}
# Dictionary containing conversion factors for temperature units
temperature_conversions = {
    "Celsius": {
        "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9 / 5) + 32,
        "Kelvin": lambda x: x + 273.15, "Rankine": lambda x: x * 9 / 5,
    },
    "Fahrenheit": {
        "Celsius": lambda x: (x - 32) * 5 / 9, "Fahrenheit": lambda x: x,
        "Kelvin": lambda x: (x + 459.67) * 5 / 9, "Rankine": lambda x: x,
    },
    "Kelvin": {
        "Celsius": lambda x: x - 273.15, "Fahrenheit": lambda x: (x * 9 / 5) - 459.67,
        "Kelvin": lambda x: x, "Rankine": lambda x: x * 5 / 9,
    },
    "Rankine": {
        "Celsius": lambda x: x * 5 / 9 - 273.15, "Fahrenheit": lambda x: x - 459.67,
        "Kelvin": lambda x: x * 5 / 9, "Rankine": lambda x: x,
    }
}
# Dictionary containing conversion factors for time units
time_conversions = {
    "Millennium": {
        "Millennium": lambda x: x, "Century": lambda x: x * 10, "Decade": lambda x: x * 100,
        "Year": lambda x: x * 1000, "Month": lambda x: x * 12000, "Week": lambda x: x * 52142.9,
        "Day": lambda x: x * 365000, "Hour": lambda x: x * 8760000, "Minute": lambda x: x * 525600000,
        "Second": lambda x: x * 3.154e+10
    },
    "Century": {
        "Millennium": lambda x: x * 0.1, "Century": lambda x: x, "Decade": lambda x: x * 10,
        "Year": lambda x: x * 100, "Month": lambda x: x * 1200, "Week": lambda x: x * 5214.29,
        "Day": lambda x: x * 36500, "Hour": lambda x: x * 876000, "Minute": lambda x: x * 52560000,
        "Second": lambda x: x * 3.154e+9
    },
    "Decade": {
        "Millennium": lambda x: x * 0.01, "Century": lambda x: x * 0.1, "Decade": lambda x: x,
        "Year": lambda x: x * 10, "Month": lambda x: x * 120, "Week": lambda x: x * 521.429,
        "Day": lambda x: x * 3650, "Hour": lambda x: x * 87600, "Minute": lambda x: x * 5256000,
        "Second": lambda x: x * 3.154e+8
    },
    "Year": {
        "Millennium": lambda x: x * 0.001, "Century": lambda x: x * 0.01, "Decade": lambda x: x * 0.1,
        "Year": lambda x: x, "Month": lambda x: x * 12, "Week": lambda x: x * 52.1429,
        "Day": lambda x: x * 365, "Hour": lambda x: x * 8760, "Minute": lambda x: x * 525600,
        "Second": lambda x: x * 3.154e+7
    },
    "Month": {
        "Millennium": lambda x: x * 8.3333e-5, "Century": lambda x: x * 8.3333e-4, "Decade": lambda x: x * 0.00833333,
        "Year": lambda x: x * 0.0833333, "Month": lambda x: x, "Week": lambda x: x * 4.34524,
        "Day": lambda x: x * 30.4167, "Hour": lambda x: x * 730.001, "Minute": lambda x: x * 43800,
        "Second": lambda x: x * 2.628e+6
    },
    "Week": {
        "Millennium": lambda x: x * 1.91757e-5, "Century": lambda x: x * 1.91757e-4, "Decade": lambda x: x * 0.00191757,
        "Year": lambda x: x * 0.019165, "Month": lambda x: x * 0.229984, "Week": lambda x: x,
        "Day": lambda x: x * 7, "Hour": lambda x: x * 168, "Minute": lambda x: x * 10080,
        "Second": lambda x: x * 604800
    },
    "Day": {
        "Millennium": lambda x: x * 2.73973e-6, "Century": lambda x: x * 2.73973e-5, "Decade": lambda x: x * 2.73973e-4,
        "Year": lambda x: x * 0.00273973, "Month": lambda x: x * 0.0328767, "Week": lambda x: x * 0.142857,
        "Day": lambda x: x, "Hour": lambda x: x * 24, "Minute": lambda x: x * 1440,
        "Second": lambda x: x * 86400
    },
    "Hour": {
        "Millennium": lambda x: x * 1.14155e-7, "Century": lambda x: x * 1.14155e-6, "Decade": lambda x: x * 1.14155e-5,
        "Year": lambda x: x * 1.14155e-4, "Month": lambda x: x * 0.00136986, "Week": lambda x: x * 0.00595238,
        "Day": lambda x: x * 0.0416667, "Hour": lambda x: x, "Minute": lambda x: x * 60,
        "Second": lambda x: x * 3600
    },
    "Minute": {
        "Millennium": lambda x: x * 1.90259e-9, "Century": lambda x: x * 1.90259e-8, "Decade": lambda x: x * 1.90259e-7,
        "Year": lambda x: x * 1.90259e-6, "Month": lambda x: x * 2.28307e-5, "Week": lambda x: x * 9.9206e-5,
        "Day": lambda x: x * 0.000694444, "Hour": lambda x: x * 0.0166667, "Minute": lambda x: x,
        "Second": lambda x: x * 60
    },
    "Second": {
        "Millennium": lambda x: x * 3.17098e-11, "Century": lambda x: x * 3.17098e-10,
        "Decade": lambda x: x * 3.17098e-9, "Year": lambda x: x * 3.17098e-8, "Month": lambda x: x * 3.80517e-7,
        "Week": lambda x: x * 1.65344e-6, "Day": lambda x: x * 1.15741e-5, "Hour": lambda x: x * 2.77778e-4,
        "Minute": lambda x: x * 0.0166667, "Second": lambda x: x
    }
}
# Dictionary containing conversion factors for volume units
volume_conversions = {
    "Cubic meter": {
        "Cubic meter": lambda x: x, "Liter": lambda x: x * 1000, "Milliliter": lambda x: x * 1e+6,
        "Imperial Gallon": lambda x: x * 219.969, "Imperial Cup": lambda x: x * 4399.38,
        "Imperial fluid ounce": lambda x: x * 35195.1, "Imperial tablespoon": lambda x: x * 56312.2,
        "Imperial teaspoon": lambda x: x * 168936, "Cubic foot": lambda x: x * 35.3147,
        "Cubic Inch": lambda x: x * 61023.7
    },
    "Liter": {
        "Cubic meter": lambda x: x * 0.001, "Liter": lambda x: x, "Milliliter": lambda x: x * 1000,
        "Imperial Gallon": lambda x: x * 0.219969, "Imperial Cup": lambda x: x * 4.39938,
        "Imperial fluid ounce": lambda x: x * 35.1951, "Imperial tablespoon": lambda x: x * 56.3122,
        "Imperial teaspoon": lambda x: x * 168.936, "Cubic foot": lambda x: x * 0.0353147,
        "Cubic Inch": lambda x: x * 61.0237
    },
    "Milliliter": {
        "Cubic meter": lambda x: x * 1e-6, "Liter": lambda x: x * 0.001, "Milliliter": lambda x: x,
        "Imperial Gallon": lambda x: x * 0.000219969, "Imperial Cup": lambda x: x * 0.00439938,
        "Imperial fluid ounce": lambda x: x * 0.0351951, "Imperial tablespoon": lambda x: x * 0.0563122,
        "Imperial teaspoon": lambda x: x * 0.168936, "Cubic foot": lambda x: x * 3.53147e-5,
        "Cubic Inch": lambda x: x * 0.0610237
    },
    "Imperial Gallon": {
        "Cubic meter": lambda x: x * 0.00454609, "Liter": lambda x: x * 4.546, "Milliliter": lambda x: x * 4546.09,
        "Imperial Gallon": lambda x: x, "Imperial Cup": lambda x: x * 20, "Imperial fluid ounce": lambda x: x * 160,
        "Imperial tablespoon": lambda x: x * 256, "Imperial teaspoon": lambda x: x * 768,
        "Cubic foot": lambda x: x * 0.160544, "Cubic Inch": lambda x: x * 277.419
    },
    "Imperial Cup": {
        "Cubic meter": lambda x: x * 0.000284131, "Liter": lambda x: x * 0.284131, "Milliliter": lambda x: x * 284.131,
        "Imperial Gallon": lambda x: x * 0.05, "Imperial Cup": lambda x: x, "Imperial fluid ounce": lambda x: x * 8,
        "Imperial tablespoon": lambda x: x * 12.8, "Imperial teaspoon": lambda x: x * 38.4,
        "Cubic foot": lambda x: x * 0.00847552, "Cubic Inch": lambda x: x * 14.6466
    },
    "Imperial fluid ounce": {
        "Cubic meter": lambda x: x * 2.8413e-5, "Liter": lambda x: x * 0.0284131, "Milliliter": lambda x: x * 28.4131,
        "Imperial Gallon": lambda x: x * 0.00625, "Imperial Cup": lambda x: x * 0.125,
        "Imperial fluid ounce": lambda x: x, "Imperial tablespoon": lambda x: x * 1.6,
        "Imperial teaspoon": lambda x: x * 4.8, "Cubic foot": lambda x: x * 0.00104084,
        "Cubic Inch": lambda x: x * 1.80469
    },
    "Imperial tablespoon": {
        "Cubic meter": lambda x: x * 1.775814121984224e-05, "Liter": lambda x: x * 0.017758141219842236,
        "Milliliter": lambda x: x * 17.758141219842237, "Imperial Gallon": lambda x: x * 0.00390625,
        "Imperial Cup": lambda x: x * 0.078125, "Imperial fluid ounce": lambda x: x * 0.625,
        "Imperial tablespoon": lambda x: x, "Imperial teaspoon": lambda x: x * 3,
        "Cubic foot": lambda x: x * 6.5915e-4, "Cubic Inch": lambda x: x * 1.14052
    },
    "Imperial teaspoon": {
        "Cubic meter": lambda x: x * 5.919401430127385e-06, "Liter": lambda x: x * 0.0059194014301273854,
        "Milliliter": lambda x: x * 5.919401430127386, "Imperial Gallon": lambda x: x * 0.00130208,
        "Imperial Cup": lambda x: x * 0.0260417, "Imperial fluid ounce": lambda x: x * 0.208333,
        "Imperial tablespoon": lambda x: x * 0.333333, "Imperial teaspoon": lambda x: x,
        "Cubic foot": lambda x: x * 2.2955e-4, "Cubic Inch": lambda x: x * 0.3950625
    },
    "Cubic foot": {
        "Cubic meter": lambda x: x * 0.028316819907857067, "Liter": lambda x: x * 28.3168,
        "Milliliter": lambda x: x * 28316.8, "Imperial Gallon": lambda x: x * 6.22884,
        "Imperial Cup": lambda x: x * 118.294, "Imperial fluid ounce": lambda x: x * 957.506,
        "Imperial tablespoon": lambda x: x * 15240, "Imperial teaspoon": lambda x: x * 45720,
        "Cubic foot": lambda x: x, "Cubic Inch": lambda x: x * 1728
    },
    "Cubic Inch": {
        "Cubic meter": lambda x: x * 1.63870758410257e-05, "Liter": lambda x: x * 0.0163871,
        "Milliliter": lambda x: x * 16.3871, "Imperial Gallon": lambda x: x * 0.00360465,
        "Imperial Cup": lambda x: x * 0.0692641, "Imperial fluid ounce": lambda x: x * 0.554113,
        "Imperial tablespoon": lambda x: x * 8.80551, "Imperial teaspoon": lambda x: x * 26.4165,
        "Cubic foot": lambda x: x * 5.78704e-4, "Cubic Inch": lambda x: x
    }
}

