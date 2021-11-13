from .constants import *
from .models import DurationStruct, DurationPrecision


def get_octoprint_url_prefix():
    return f"{OCTOPRINT_PROTOCOL}://{OCTOPRINT_ADDRESS}:{OCTOPRINT_PORT}"

def build_url(prefix: str, api_url: str):
    api_url_ = api_url.strip("/")
    return f"{prefix}/{api_url_}"

def convert_seconds(seconds: int) -> DurationStruct:
    if seconds is None or not isinstance(seconds, int) or seconds < 0:
        raise ValueError("Parameter seconds has invalid type or value")
    days = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return DurationStruct(days, hours, minutes, seconds)

def time_struct_to_text(time_struct: DurationStruct, precision:DurationPrecision=DurationPrecision.minutes):
    results = []                    # keep a list of texts, will join with comma
    if time_struct.is_0():
        return '0 seconds'
    if time_struct.days != 0:
        results.append(f"{time_struct.days} days")
    if time_struct.hours != 0 and precision >=DurationPrecision.hours:
        results.append(f"{time_struct.hours} hours")
    if time_struct.minutes != 0 and precision >=DurationPrecision.minutes:
        results.append(f"{time_struct.minutes} minutes")
    if time_struct.seconds != 0 and precision >=DurationPrecision.seconds:
        results.append(f"{time_struct.seconds} seconds")
    return ", ".join(results)