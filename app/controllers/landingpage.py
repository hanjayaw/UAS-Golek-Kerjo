from flask import Flask, render_template, request, session
from app import app, RunSelect

# Code di bawah sini

@app.route('/')
def landingpage():
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    return render_template("index.html")