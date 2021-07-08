from bottle import Bottle, route, get, response, request, redirect
from controllers import account

app = Bottle()

# route setting
app.mount('/accounts', account.app)