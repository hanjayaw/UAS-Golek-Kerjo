from flask import Flask, render_template, request
from app import app

# Code di bawah sini

@app.route('/profile')
def profile():
    return render_template("profile.html")

