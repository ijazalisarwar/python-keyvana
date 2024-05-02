import logging
import json
import urllib.request

import azure.functions as func


def main(req: func.HttpRequest, outputblob: func.Out[func.InputStream]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    response_data = {}
    try:
        req_body = req.get_json()
        logging.info(req_body)
        base_url = req_body.get('base_url')
        end_point = req_body.get('end_point')
        vin_id = req_body.get('vin_id')
        api_key = req_body.get('api_key')
        request_url = base_url + end_point + vin_id + "?api_key=" + api_key
        logging.info("request_url:" + request_url)
        contents = urllib.request.urlopen(request_url).read()
        outputblob.set(contents)
        response_data["message"] = "updated."
    except Exception as ex:
        response_data["message"] = 'Exception: ' + str(ex)
        logging.info('Exception: ' + str(ex))

    return func.HttpResponse(
            json.dumps(response_data),
            status_code=200
    )
