import os, json
from bottle import route, run, Bottle, get, error, HTTPResponse
from routes import api
from dotenv import load_dotenv
from service import auth

load_dotenv()
app = Bottle()

# Setup basic auth
auth.setup_auth()
app.add_hook('before_request', auth.is_valid)

@app.error(404)
def error404(error):
  res = HTTPResponse(status=404, body=json.dumps({'message': 'not found'}))
  res.set_header('Content-Type', 'application/json')
  return res

@app.error(500)
def error404(error):
  res = HTTPResponse(status=500, body=json.dumps({'message': 'internal server error'}))
  res.set_header('Content-Type', 'application/json')
  return res

# root setting
@app.get('/')
def index():
  return {'status': 'ok'}

# start up web api
if __name__ == '__main__':

  # load routes
  app.mount('/api', api.app)

  # set options
  isDebugMode = False
  autoReload = False
  if os.environ.get("EVN") != 'production':
    isDebugMode = True
    autoReload = True

  print("isDebugMode", isDebugMode)
  print("autoReload", autoReload)

  # start
  app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
    debug=isDebugMode,
    reloader=autoReload
  )