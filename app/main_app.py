from flask import Flask
from .pages.index import index_pages
from .pages.cart import cart_pages
from .pages.checkout import checkout_pages

app = Flask(__name__, static_folder="../public", template_folder="../templates")
app.secret_key = "gxnMaYjinQ27DeBwgKsDyuDQO" #secret keyul e necesar pentru session

app.register_blueprint(index_pages) #adauga rutele necesare
app.register_blueprint(cart_pages)
app.register_blueprint(checkout_pages)