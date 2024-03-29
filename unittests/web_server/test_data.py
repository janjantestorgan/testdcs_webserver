import pytest

from pydantic import ValidationError

from tracker_dcs_web.web_server.data import SensorData

user = "candan"
password = "cms"


def test_sensor_data():
    the_data = [27.0, 51, 18.1, 40.0]
    _ = SensorData(data=the_data)
    the_data = [27.0, 51, 18.1, 40.0, 33]
    with pytest.raises(ValidationError):
        _ = SensorData(data=the_data)
