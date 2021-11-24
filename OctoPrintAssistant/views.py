import re
# Create your views here.
from django.http import HttpResponse

from .constants import MASTER_NAME, GENERAL_OCTOPRINT_HEADER
from django.views.decorators.http import require_http_methods
import requests
import io
from .utils import get_octoprint_url_prefix, build_url, time_struct_to_text, convert_seconds, \
    get_job_status_response, send_connection_request, select_file, get_current_file_path, \
    retrieve_all_files_paths, send_command
from .models import DurationPrecision
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@require_http_methods(['GET'])
def index(request):
    return HttpResponse("""
    Hi, you are calling the API of OctoPrint Assistant.
    Check https://github.com/HuakunShen/OctoPrint-Assitant for the full API documentation.
    """)


@require_http_methods(['GET'])
def octoprint_state(request):
    url = build_url(get_octoprint_url_prefix(), '/api/connection')
    res = requests.get(url, headers=GENERAL_OCTOPRINT_HEADER)
    if res.status_code != 200:
        return HttpResponse(f"Request to OctoPrint failed: Status Code={res.status_code}")
    res_json = res.json()
    state = res_json['current']['state']
    return HttpResponse(state)


@require_http_methods(['POST'])
def octoprint_connect(request):
    return send_connection_request({"command": "connect"})


@require_http_methods(['POST'])
def octoprint_disconnect(request):
    return send_connection_request({"command": "disconnect"})


@require_http_methods(['GET'])
def octoprint_job_status(request):
    res = get_job_status_response()
    if res.status_code != 200:
        return HttpResponse(f"Request to OctoPrint failed: Status Code={res.status_code}")
    res_json = res.json()
    state = res_json['state']
    print_time = res_json['progress']['printTime']
    print_time_left = res_json['progress']['printTimeLeft']
    file_name = res_json['job']['file']['name']
    response = io.StringIO()

    if print_time is None or print_time_left is None:
        response.write(f"{state}, Not Printing")
    else:
        print_time_text = time_struct_to_text(convert_seconds(print_time), DurationPrecision.minutes)
        print_time_left_text = time_struct_to_text(convert_seconds(print_time_left), DurationPrecision.minutes)
        response.write(f"Dear {MASTER_NAME}, I am {state}. ")
        response.write(f"The file I am printing is {file_name}. ")
        response.write(f"I Have printed for {print_time_text}, ")
        response.write(f"and printing time left is {print_time_left_text}\n")
    return HttpResponse(response.getvalue(), content_type="text/plain")


@require_http_methods(['GET'])
def octoprint_retrieve_files(request):
    paths = retrieve_all_files_paths()
    response_text = f"You have {len(paths)} files. "

    for i, path in enumerate(paths):
        response_text += f"The {i + 1}th file is, {path}. "
    return HttpResponse(response_text)


@require_http_methods(['POST'])
def octoprint_select(request):
    index = request.POST.get("index")
    match = re.match(r"^\d+$", index)
    file_paths = retrieve_all_files_paths()
    if match is None or int(index) > len(file_paths) or int(index) < 1:
        return HttpResponse("Invalid Index")
    file_path = file_paths[int(index) - 1]
    res = select_file(file_path)
    if res.status_code == 204:
        return HttpResponse(f"{file_path} selected", status=200)
    else:
        return HttpResponse("Error: Not Selected", status=res.status_code)


@require_http_methods(['POST'])
def octoprint_shift_job(request):
    cur_file_path = get_current_file_path()
    if cur_file_path is None:
        return HttpResponse("No file selected")
    file_paths = retrieve_all_files_paths()
    index = file_paths.index(cur_file_path)
    next_index = (index + 1) % len(file_paths)
    to_select_file_path = file_paths[next_index]
    res = select_file(to_select_file_path)
    if res.status_code != 204:
        return HttpResponse("Fail to shift", status=400)
    return HttpResponse(f"File shifted. Current file selected is {to_select_file_path}")


@require_http_methods(['POST'])
def octoprint_job_cancel(request):
    res = send_command(command="cancel")
    response_text = res.text if res.status_code != 204 else f"Yes {MASTER_NAME}, Job Cancelled"
    return HttpResponse(response_text, status=200)


@require_http_methods(['POST'])
def octoprint_job_start(request):
    res = send_command(command="start")
    response_text = res.text if res.status_code != 204 else f"Yes {MASTER_NAME}, Job Started"
    return HttpResponse(response_text, status=200)


@require_http_methods(['POST'])
def octoprint_job_toggle(request):
    res = send_command(command="pause", action="toggle")
    response_text = res.text if res.status_code != 204 else f"Yes {MASTER_NAME}, Job Toggled"
    return HttpResponse(response_text, status=200)
