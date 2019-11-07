from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Designs and Contact."""
    return render_template('index.html')

@app.route('/designs')
def fortune_form():
    """Displays Designs."""
    return render_template('designs.html')

@app.route('/contact')
def fortune_results():
    """Displays contact information."""
    return render_template('contact.html')
       
