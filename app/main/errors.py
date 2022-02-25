from flask import render_template
from .import main

@main.app_errorhandler(404)
def four_Ow_Four(error):
    """
    Function to render the 404 error page
    """
    return render_template('fourOwFour.html'),404
    