from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sentinelsatapp.managers import get_sentinel_api_data
import json


def home(request):

    return render(request, "index.html", {})


@csrf_exempt
def load_sentinel(request):
    success, message, errors, resp = False, "", [], []
    if request.method == "POST":
        data = json.loads(request.body)
        errors, v_success = validation(data)
        if v_success:
            resp = get_sentinel_api_data(
                data["polygon"],
                data["start"].replace("-", ""),
                data["end"].replace("-", ""),
                data["sentinel"],
                data["cloudcoverpercentage_start"],
                data["cloudcoverpercentage_end"],
            )
            success = True
            message = "Data save success"
        else:
            success = False
            message = "Please complete the fields in errors data!"
    response = {
        "success": success,
        "message": message,
        "errors": errors,
        "resp": resp,
    }
    return JsonResponse(response, safe=False)


def validation(data):
    errors, success = [], True
    validation_data = [
        "polygon",
        "start",
        "end",
        "sentinel",
        "cloudcoverpercentage_start",
        "cloudcoverpercentage_end",
    ]
    for item in validation_data:
        if item not in data:
            errors.append(item)

    if len(errors) > 0:
        success = False

    return errors, success


"""
# JSON TO POST DATA

{
    "polygon": "POLYGON ((34.322010 0.401648,36.540989 0.876987,36.884121 -0.747357,34.664474 -1.227940,34.322010 0.401648))",
    "start": "2015-12-12",
    "end": "2016-01-01",
    "sentinel": "Sentinel-2",
    "cloudcoverpercentage_start": 0,
    "cloudcoverpercentage_end": 3
}
"""
