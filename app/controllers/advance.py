from flask import Flask, render_template, request, session
from app import app, RunSelect, ExecuteCMD, RunSelectOne


@app.route('/advance', methods=["POST", "GET"])
def advance():
    if request.method == "POST":
            searching = request.form["search"]
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND tipe_job like \'%"+searching+"%\' OR nama_perusahaan like \'%"+searching+"%\'"
            results = RunSelect(qry)
            return render_template('advance.html', results = results)
    return render_template('advance.html')