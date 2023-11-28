from flask import Flask, request, jsonify
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

# API-PRODUCTS

@app.get("/api/about")
def about():
    return jsonify({"version": 1.03, "name": 'stable3'})

@app.get("/api/about/me")
def about_me():
    return jsonify(me)

@app.get("/api/product")
def get_products():
    return jsonify(catalog)

@app.post("/api/product")
def save_product():
    product = request.get_json()
    # todo: save to db instead of in the memory
    catalog.append(product)
    return jsonify({"status": "saved"})

@app.get("/api/product/count")
def product_count():
    total = len(catalog)
    return jsonify({"total": total})

@app.get("/api/reports/total")
def get_total():
    total = sum(product.get("price", 0) for product in catalog)
    return jsonify({"value": total})

@app.get("/api/categories")
def get_categories():
    categories = set(product.get("category") for product in catalog if "category" in product)
    return jsonify({"categories": list(categories)})

# get /api/product/category/fruit
@app.get("/api/product/category/<category>")
def product_by_category(category):
    filtered_products = [product for product in catalog if "category" in product and product["category"].lower() == category.lower()]
    return jsonify({"category": category, "products": filtered_products})



@app.get("/api/product/search/<title>")
def product_search(title):
    # Add logic to filter products by title (case-insensitive)
    filtered_products = [product for product in catalog if "title" in product and title.lower() in product["title"].lower()]
    return jsonify({"title": title, "products": filtered_products})

app.run(debug=True)
