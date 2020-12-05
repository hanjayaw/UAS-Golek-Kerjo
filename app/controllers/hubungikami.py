from flask import Flask, render_template, request
from app import app

# Code di bawah sini

@app.route('/hubungikami')
def hubungi():
    return render_template("contact.html")