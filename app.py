import json, base64
from unittest import result

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


from components.db.db import AWS_RDS
from components.fractals import Mandelbrot




def encode_params(value):
  return base64.urlsafe_b64encode(json.dumps(value).encode()).decode()

def decode_params(encoded_value):
  return base64.urlsafe_b64decode(encoded_value).decode()





app = Flask("Fractals API")

CORS(app)



def Error(msg=None):
  return {"status": "failed", "msg":msg}




@app.route("/")
def test():
  return "Hello, World!"


#@app.route("/user/<username>", methods=['GET', 'POST'])

@app.route("/user/<username>")
def user_profile(username):
  # handle cookies to tell if the user is logged in.
  # If the user is logged in, show private projects as well.
  return username


@app.route("/user/<username>/")
def user_profile_route_1(username):
  return user_profile(username)



@app.route("/user/<username>/project/all")
def user_projects(username):
  # handle cookies to tell if the user is logged in.
  # If the user is logged in, show private projects as well.
  if not AWS_RDS.ForceConnect(): return Error("Could Not Connnect To Database.")
  
  results = AWS_RDS.select_user_id(username)
  if not results: return Error(f"The exists no account with username {username}") 

  data = {}
  data['user_id'] = results['id']
  data['public']=True

  is_owner = False
  if is_owner:
    del data['public']

  results = AWS_RDS.load_fractal_project(data)
  return jsonify(results)






@app.route("/user/<username>/project/<project_id>")
def user_project(username, project_id):
  if not AWS_RDS.ForceConnect(): return Error("Could Not Connnect To Database.")

  results = AWS_RDS.select_user_id(username)
  if not results: return Error(f"The exists no account with username {username}") 

  data = {}
  data['id'] = int(project_id)
  data['public']=True
  data['user_id'] = results['id']

  return jsonify(AWS_RDS.load_fractal_project(data))


@app.route('/engine/mandelbrot')
def generate_mandelbrot():

  # Handle Parameters and their types and default values
  data = {
    'width': request.args.get('width', default=100, type=int),
    'height': request.args.get('height', default=100, type=int),

    'iters': request.args.get('iters', default=10, type=int),
    'zoom': request.args.get('zoom', default=200, type=int),
    'bounds': request.args.get('bounds', default=100, type=int),

    'camx': request.args.get('camx', default=2, type=int),
    'camy': request.args.get('camy', default=1.5, type=int),
  }

  set = Mandelbrot.generate(**data)

  return json.dumps(set)





# On load grab a random fractal from the database
