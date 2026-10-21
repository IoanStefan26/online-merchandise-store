from flask import Blueprint, render_template
from ..model.products import get_all_products

index_pages = Blueprint("index", __name__)

@index_pages.route("/")
def index_page():
    products = get_all_products()  #luam produsele de la products.py
    return render_template("index.html", products = products)  #apoi le trimitem catre Jinja

@index_pages.route("/contact")
def contact_page():
    return render_template("contact.html")

