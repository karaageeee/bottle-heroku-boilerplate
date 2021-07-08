from bottle import Bottle, get

app = Bottle()

@app.get('/')
def list():
  return {'accounts': [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]}
