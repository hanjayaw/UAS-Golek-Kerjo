from flask import Flask, render_template, request, session
from app import app, RunSelect, ExecuteCMD, RunSelectOne


@app.route('/advance', methods=["POST", "GET"])
def advance():   
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    if request.method == "POST":
        searching = request.form.get("search", "")
        jenisjobs = request.form.get("durasi", "")
        tipejobs = request.form.get("jenis", "")
        namakota = request.form.get("namakota", "")   
        gajimin = request.form.get("gaji-minim", "")   
        gajimax = request.form.get("gaji-max", "")
        if searching == "":
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job LIKE \'%"+jenisjobs+"%\' AND tipe_job LIKE \'%"+tipejobs+"%\' AND kota LIKE \'%"+namakota+"%\' OR minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1"
        elif searching != "" and jenisjobs == "" and tipejobs == "" and namakota == "" and gajimin == "" and gajimax == "":
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (UPPER(tipe_job) LIKE UPPER(\'%"+searching+"%\') OR UPPER(nama_perusahaan) LIKE UPPER(\'%"+searching+"%\'))"
        else:
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (UPPER(tipe_job) LIKE UPPER(\'%"+searching+"%\') OR UPPER(nama_perusahaan) LIKE UPPER(\'%"+searching+"%\')) AND (duration_job LIKE \'"+jenisjobs+"\' OR tipe_job LIKE \'"+tipejobs+"\' OR kota LIKE \'"+namakota+"\' OR minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1)"
        results = RunSelect(qry)
        return render_template('advance.html', results = results)
    return render_template('advance.html') 

@app.route('/freelance')
def freelance():
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job = 'Freelance'"
    results = RunSelect(qry)
    return render_template('hasilcari.html', results = results)

@app.route('/parttime')
def parttime():
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job = 'Part Time'"
    results = RunSelect(qry)
    return render_template('hasilcari.html', results = results)

@app.route('/fulltime')
def fulltime():
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job = 'Full Time'"
    results = RunSelect(qry)
    return render_template('hasilcari.html', results = results)