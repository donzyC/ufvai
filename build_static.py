import os
import shutil
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/why-department')
def why_department():
    return render_template('why-department.html')

@app.route('/problem-opportunity')
def problem_opportunity():
    return render_template('problem-opportunity.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/ai-ethics')
def ai_ethics():
    return render_template('ai-ethics.html')

@app.route('/ai-teaching')
def ai_teaching():
    return render_template('ai-teaching.html')

@app.route('/interface')
def interface():
    return render_template('interface.html')

@app.route('/programming')
def programming():
    return render_template('programming.html')

@app.route('/programming-languages')
def programming_languages():
    return render_template('programming-languages.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/get-involved')
def get_involved():
    return render_template('get-involved.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/intranet-integration')
def intranet_integration():
    return render_template('intranet-integration.html')

# Create a test client
client = app.test_client()

# Define the routes to capture
routes = [
    '/',
    '/why-department',
    '/problem-opportunity',
    '/plan',
    '/ai-ethics',
    '/ai-teaching',
    '/interface',
    '/programming',
    '/programming-languages',
    '/contact',
    '/get-involved',
    '/apply',
    '/intranet-integration'
]

# Create the static directory
static_dir = 'static_site'
if os.path.exists(static_dir):
    shutil.rmtree(static_dir)
os.makedirs(static_dir)

# Copy static files
shutil.copytree('static', os.path.join(static_dir, 'static'))

# Generate static HTML files
for route in routes:
    # Get the response
    response = client.get(route)
    
    # Create the directory if it doesn't exist
    path = route.lstrip('/')
    if path == '':
        path = 'index'
    
    # Create the directory structure
    os.makedirs(os.path.join(static_dir, os.path.dirname(path)), exist_ok=True)
    
    # Write the HTML to a file
    with open(os.path.join(static_dir, f"{path}.html"), 'w', encoding='utf-8') as f:
        f.write(response.data.decode('utf-8'))
    
    print(f"Generated {path}.html")

print("Static site generation complete!") 