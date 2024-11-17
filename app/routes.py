from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def auth():
    return render_template('auth.html')

@main.route('/privacy')
def privacy():
    return "Politique de confidentialité"

@main.route('/terms')
def terms():
    return "Conditions d'utilisation"

@main.route('/legal')
def legal():
    return "Mentions légales"

@main.route('/contact')
def contact():
    return "Contact"