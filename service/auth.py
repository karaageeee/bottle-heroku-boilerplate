import sys, os, json
from bottle import request, HTTPResponse, parse_auth

def setup_auth():
  if os.environ.get("BASIC_AUTH_USER", "") == "" or os.environ.get("BASIC_AUTH_PASS", "") == "":
    print("ERROR : BASIC_AUTH_USER or BASIC_AUTH_PASS is empty")
    sys.exit()

def invalid_request_response():
  res = HTTPResponse(status=400, body=json.dumps({'message': 'invalid request'}))
  res.set_header('Content-Type', 'application/json')
  raise res

def is_valid():
  # BASIC認証のユーザ名とパスワードをチェック
  if request.headers.get('Authorization') is None:
    raise invalid_request_response()

  auth = request.headers.get('Authorization')
  username, password = parse_auth(auth)
  if username != os.environ.get("BASIC_AUTH_USER") or password != os.environ.get("BASIC_AUTH_PASS"):
    raise invalid_request_response()