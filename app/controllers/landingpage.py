from flask import Flask, render_template, request
from app import app

# Code di bawah sini

@app.route('/')
def landingpage():
    return render_template("index.html")