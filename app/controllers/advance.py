from flask import Flask, render_template, request, session
from app import app, RunSelect, ExecuteCMD, RunSelectOne


@app.route('/advance', methods=["POST", "GET"])
def advance():
    return render_template('advance.html')