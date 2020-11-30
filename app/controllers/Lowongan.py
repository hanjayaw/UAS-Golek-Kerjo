from flask import Flask, render_template, request
from app import app

@app.route('/lowongan', methods = ["POST", "GET"])
def lowongan():
    return render_template('lowongan.html')
# Code di bawah sini