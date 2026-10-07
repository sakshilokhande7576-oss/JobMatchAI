import base64
from app.web import app


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method")
    if not method:
        method = event.get("httpMethod", "GET")

    raw_path = event.get("rawPath", event.get("path", "/"))

    headers = event.get("headers") or {}

    body = event.get("body") or ""
    if event.get("isBase64Encoded"):
        body = base64.b64decode(body).decode("utf-8")

    query_string = event.get("rawQueryString", "")

    environ = {
        "REQUEST_METHOD": method,
        "PATH_INFO": raw_path,
        "QUERY_STRING": query_string,
        "SERVER_NAME": headers.get("host", "lambda"),
        "SERVER_PORT": "443",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "wsgi.url_scheme": "https",
        "wsgi.version": (1, 0),
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
        "wsgi.input": __import__("io").BytesIO(body.encode("utf-8")),
        "CONTENT_LENGTH": str(len(body.encode("utf-8"))),
    }

    for key, value in headers.items():
        header_key = key.upper().replace("-", "_")

        if header_key == "CONTENT_TYPE":
            environ["CONTENT_TYPE"] = value
        elif header_key == "CONTENT_LENGTH":
            environ["CONTENT_LENGTH"] = value
        else:
            environ[f"HTTP_{header_key}"] = value

    response_status = []
    response_headers = []

    def start_response(status, response_headers_list, exc_info=None):
        response_status.append(status)
        response_headers.extend(response_headers_list)

    response_body = app.wsgi_app(environ, start_response)

    body_bytes = b"".join(response_body)

    if hasattr(response_body, "close"):
        response_body.close()

    status_code = int(response_status[0].split()[0])

    response = {
        "statusCode": status_code,
        "headers": dict(response_headers),
        "body": body_bytes.decode("utf-8"),
        "isBase64Encoded": False,
    }

    return response