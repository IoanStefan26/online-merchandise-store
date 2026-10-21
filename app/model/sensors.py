"""
Data model for IoT sensors.
"""

iot_data = {
    "ext_temp": 0,
    "int_temp": 0,
    "ext_hum": 0,
    "int_hum": 0,
    "rain": 0,
}


def fetch_iot_data():
    return iot_data


def set_iot_data(data):
    # TODO: update the dictionary with the new data
    pass

