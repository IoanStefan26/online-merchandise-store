from app.main_app import app

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True, port=5000) #se ruleaza pe 5000 deci e bine
    # permite accesarea aplicatiei si din afara containerului docker

