from flask import Flask, render_template
from flask import Response
from data.bitcoin import get_bitcoin_pricing
from time import time
from flask import g
# import logging
# logging.basicConfig(
#     filename='yourlogfile.log', 
#     level=logging.INFO,
# )
app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")

@app.route("/pricing")
def pricing():
    response = Response(get_bitcoin_pricing(), mimetype="text/event-stream")
    return response

@app.before_request
def before_request():
  g.start = time()

@app.after_request
def after_request(response):
    diff = time() - g.start
    print("time taken ==============>"+str(diff))
    return response