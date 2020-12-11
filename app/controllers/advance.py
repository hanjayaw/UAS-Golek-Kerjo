from flask import Flask, render_template, request, session
from app import app, RunSelect, ExecuteCMD, RunSelectOne


@app.route('/advance', methods=["POST", "GET"])
def advance():   
    qrykota = "SELECT kota from kota ORDER BY kota"
    kota = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    jenis = RunSelect(qryjenis)
    if request.method == "POST":
        searching = request.form.get("search", "")
        jenisjobs = request.form.get("durasi", "")
        tipejobs = request.form.get("jenis", "")
        namakota = request.form.get("namakota", "")   
        gajimin = request.form.get("gaji-minim", "")   
        gajimax = request.form.get("gaji-max", "")
        if searching == "":
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job LIKE \'%"+jenisjobs+"%\' AND tipe_job LIKE \'%"+tipejobs+"%\' AND kota LIKE \'%"+namakota+"%\' AND minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1"
        elif searching != "" and jenisjobs == "" and tipejobs == "" and namakota == "" and gajimin == "" and gajimax == "":
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (UPPER(tipe_job) LIKE UPPER(\'%"+searching+"%\') OR UPPER(nama_perusahaan) LIKE UPPER(\'%"+searching+"%\'))"
        else:
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (UPPER(tipe_job) LIKE UPPER(\'%"+searching+"%\') OR UPPER(nama_perusahaan) LIKE UPPER(\'%"+searching+"%\')) AND (duration_job LIKE \'"+jenisjobs+"\' OR tipe_job LIKE \'"+tipejobs+"\' OR kota LIKE \'"+namakota+"\' OR minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1)"
        results = RunSelect(qry)
        return render_template('advance.html', results = results, kota = kota, jenis = jenis)
    return render_template('advance.html', kota = kota, jenis = jenis) 