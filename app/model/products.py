PRODUCTS = [  # lista de produse
	{
		"id": "hanorac",
		"name": "Hanorac Florin Salam",
		"description": "hanorac cu regele nostru, Salam",
		"price": 299.99,
		"image": "images/hanorac.png",
	},
	{
		"id": "masa",
		"name": "Masa Florin Salam",
		"description": "Masa la care stai cu seful, Salam",
		"price": 369.99,
		"image": "images/masa.png",
	},
	{
		"id": "prosop",
		"name": "Prosop Florin Salam",
		"description": "Florin salam te sterge de tristete",
		"price": 79.99,
		"image": "images/prosop.png",
	},
	{
		"id": "ghiozdan",
		"name": "Ghiozdan Florin Salam",
		"description": "Vericul Florin Salam iti are spatele",
		"price": 99.99,
		"image": "images/ghiozdan.png",
	},
]

def get_all_products(): #returneaza toate produsele pt ruta FLASK
	return PRODUCTS

def get_product_by_id(product_id): #cauta un produs dupa id si il intoarce
	for product in PRODUCTS:
		if product["id"] == product_id:
			return product
	return None