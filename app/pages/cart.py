from flask import Blueprint, session, request, redirect, render_template
from ..model.products import get_all_products, get_product_by_id

cart_pages = Blueprint("cart", __name__)

@cart_pages.route("/cart")
def cart_page():
	cart = session.get("cart", {})
	products = []

    #se parcurge cosul si se transforma in produse afisabile
	for product_id, quantity in cart.items():
		product = get_product_by_id(product_id)
		if product is not None:
			products.append({
				"id": product["id"],
				"name": product["name"],
				"price": product["price"],
				"quantity": quantity,
				"total": product["price"] * quantity,
			})

	total = sum(product["total"] for product in products) #calculeaza pretul total
	return render_template("cart.html", products=products, total=total) 
    #incarca html-ul si ii trimite cele 2 variabile

@cart_pages.route("/cart/add-item", strict_slashes=False) #definieste pagina cosului
#punem strict_slashes false pt ca din enunt parea ca ar trebui sa fie valabile ambele tipuri de adrese
def add_item():
	product_id = request.args.get("id")
	product = get_product_by_id(product_id)

	if product is None: #daca cineva intra manual pe un produs inexistent este trimit 
        #la calea principala =>programare defensiva
		return redirect("/")

	cart = session.get("cart", {})
	cart[product_id] = cart.get(product_id, 0) + 1
	session["cart"] = cart

	return redirect("/cart")

@cart_pages.route("/cart/remove-item", strict_slashes=False)
def remove_item(): #functie simpla de sters din cos
	product_id = request.args.get("id")
	cart = session.get("cart", {})

	if product_id in cart:
		cart[product_id] = cart[product_id] - 1

		if cart[product_id] <= 0:
			del cart[product_id]

	session["cart"] = cart #salvam

	return redirect("/cart")