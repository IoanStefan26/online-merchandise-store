from flask import Blueprint, request, render_template, session, redirect
from ..model.products import get_product_by_id
from pathlib import Path
from datetime import datetime
import json

checkout_pages = Blueprint("checkout", __name__)
ORDERS_DIR = Path(__file__).resolve().parents[2] / "submitted-data"
#folderul pentru comenzi

@checkout_pages.route("/checkout", methods=["GET", "POST"]) #cererile pe care le accepta
def checkout_page():
	cart = session.get("cart", {})
	products = []

	for product_id, quantity in cart.items():
		product = get_product_by_id(product_id)
		if product is not None: #cosul simplu e transformat in lista detaliata
			products.append({
				"id": product["id"],
				"name": product["name"],
				"price": product["price"],
				"quantity": quantity,
				"total": product["price"] * quantity,
			})

	total = sum(product["total"] for product in products)

	if request.method == "POST": #verifica daca persoana a trimis formularul
		order = {
			"full_name": request.form.get("full_name"),
			"email": request.form.get("email"),
			"phone": request.form.get("phone"),
			"address": request.form.get("address"),
			"payment_method": request.form.get("payment_method"),
			"products": products,
			"total": total,
		}

		print(order) #afiseaza comanda in terminal, NU browser
		
		ORDERS_DIR.mkdir(exist_ok=True)
	
		file_name = datetime.now().strftime("order-%Y-%m-%d_%H-%M-%S-%f.json")
		file_path = ORDERS_DIR / file_name
	
		with open(file_path, "w", encoding="utf-8") as f:
			json.dump(order, f, indent=4, ensure_ascii=False)
	
		session["cart"] = {} #cosul se goleste dupa plasarea comenzii

		return render_template("checkout_success.html", order=order) #returnul pe cazul POST, succes
	return render_template("checkout.html", products=products, total=total) #pagina normala de checkout