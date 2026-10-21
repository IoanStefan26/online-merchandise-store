# Online Merchandise Store

A merchandise storefront built with Python and Flask, featuring a product catalogue, a session-based shopping cart, and an order submission workflow. The application uses a Florin Salam-themed catalogue and was developed as a university coursework project, extending a Flask laboratory starter template.

## Features

- Product catalogue with images, descriptions, and prices.
- Session-based shopping cart with quantity controls and automatic total calculation.
- Checkout form for customer details and payment method selection.
- Order persistence as individual JSON files and automatic cart clearing after submission.
- Modular routing through Flask Blueprints and shared page layouts using Jinja templates.
- Docker support for containerised execution.

## Technology Stack

Python 3.12 · Flask 3 · Jinja · HTML · CSS · Docker

## Run Locally

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 server.py
```

On Windows PowerShell, activate the virtual environment with `.\.venv\Scripts\Activate.ps1` instead.

Open [http://localhost:5000](http://localhost:5000).

## Run with Docker

```bash
docker build -t online-merchandise-store .
docker run --rm -p 5000:5000 online-merchandise-store
```

Orders created inside the container are removed when the container is deleted unless the order directory is mounted to persistent storage.

## Project Structure

```text
app/
  main_app.py       Flask application and Blueprint registration
  model/           Product catalogue and lookup functions
  pages/           Catalogue, cart, and checkout routes
public/            Stylesheets and product images
templates/         Jinja page templates
server.py          Application entry point
requirements.txt   Python dependencies
Dockerfile         Container configuration
```

Submitted orders are written to `app/submitted-data/`, which is created automatically when an order is placed.

## Scope

This project demonstrates a complete catalogue-to-order workflow for educational purposes. Payment method selection is recorded with the order; no online payment processing is implemented. The supplied entry point runs Flask's development server with debug mode enabled.

## Author

Ioan Ștefan
