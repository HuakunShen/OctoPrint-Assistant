import json

from django.http import HttpResponse

from .constants import *
from .constants import GENERAL_OCTOPRINT_HEADER
from .models import DurationStruct, DurationPrecision
from typing import Dict, List, Union
import requests
import logging
logger = logging.getLogger(__name__)


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


def time_struct_to_text(time_struct: DurationStruct, precision: DurationPrecision = DurationPrecision.minutes):
    results = []                    # keep a list of texts, will join with comma
    if time_struct.is_0():
        return '0 seconds'
    if time_struct.days != 0:
        results.append(f"{time_struct.days} days")
    if time_struct.hours != 0 and precision >= DurationPrecision.hours:
        results.append(f"{time_struct.hours} hour{'s' if time_struct.hours > 1 else ''}")
    if time_struct.minutes != 0 and precision >= DurationPrecision.minutes:
        results.append(f"{time_struct.minutes} minutes")
    if time_struct.seconds != 0 and precision >= DurationPrecision.seconds:
        results.append(f"{time_struct.seconds} seconds")
    return ", ".join(results)


def get_job_status_response() -> requests.models.Response:
    url = build_url(get_octoprint_url_prefix(), '/api/job')
    return requests.get(url, headers=GENERAL_OCTOPRINT_HEADER)


def parse_files_path(files: Dict) -> List[str]:
    paths = []
    for file in files:
        if file['type'] != 'folder':
            paths.append(file['path'])
        else:
            paths.extend(parse_files_path(file['children']))
    return paths


def send_connection_request(payload: Dict):
    url = build_url(get_octoprint_url_prefix(), '/api/connection')
    res = requests.post(url, headers=GENERAL_OCTOPRINT_HEADER, data=json.dumps(payload))
    if res.status_code == 204:
        return HttpResponse(f"Disconnected", content_type="text/plain")
    else:
        logger.error(res.content)
        return HttpResponse(f"Error, not disconnected", status=res.status_code)


def select_file(name: str) -> requests.models.Response:
    url = build_url(get_octoprint_url_prefix(), f'/api/files/local/{name}')
    payload = json.dumps({"command": "select", "print": False})
    return requests.post(url, headers=GENERAL_OCTOPRINT_HEADER, data=payload)


def get_current_file_path() -> Union[None, str]:
    res = get_job_status_response()
    if res.status_code != 200:
        return None
    res_json = res.json()
    filename = res_json['job']['file']['path']
    return filename


def retrieve_all_files_paths():
    url = build_url(get_octoprint_url_prefix(), '/api/files')
    res = requests.get(url, headers=GENERAL_OCTOPRINT_HEADER, params={"recursive": True})
    files = res.json()['files']
    paths = parse_files_path(files)
    return paths


def send_command(command: str, action: str = None):
    url = build_url(get_octoprint_url_prefix(), '/api/job')
    json_data = {"command": command, "action": action}
    if action is not None:
        json_data.update({"action": action})
    return requests.post(url, headers=GENERAL_OCTOPRINT_HEADER, json=json_data)
