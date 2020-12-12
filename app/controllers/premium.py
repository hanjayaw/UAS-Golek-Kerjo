from flask import Flask, render_template, request
from app import app

# Code di bawah sini

@app.route('/premium')
def premium():
    return render_template("pembayaran.html")