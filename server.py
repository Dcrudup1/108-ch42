from flask import Flask
import json
from config import me
from mock_data import catalog

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from Flask!!"


@app.get("/test")
def test():
    return "this is a test page"



#######################################
##########API-PRODUCTS #############
#######################################


@app.get("/api/about")
def about():
    return json.dumps({"version": 1.03, "name": 'stable3'})



@app.get("/api/about/me")
def about_me():

    return json.dumps(me)


@app.get("/api/product")
def get_products():
    return json.dumps(catalog)


@app.get("/api/product/count")
def product_count():
    total = len(catalog)
    return json.dumps({"total": total})


app.run (debug=True)
