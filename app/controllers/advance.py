from flask import Flask, render_template, request, session
from app import app, RunSelect, ExecuteCMD, RunSelectOne


@app.route('/advance', methods=["POST", "GET"])
def advance():
    qrykota = "SELECT kota from kota ORDER BY kota"
    kota = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    jenis = RunSelect(qryjenis)
    if request.method == "POST":
        searching = request.form["search"]
        jenisjobs = request.form.get("durasi")
        tipejobs = request.form.get("tiptipe")
        namakota = request.form.get("namakota")
        
        #qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (tipe_job LIKE \'%"+searching+"%\' OR nama_perusahaan LIKE \'%"+searching+"%\') AND duration_job LIKE \'%"+jenisjobs+"%\' AND tipe_job LIKE \'%"+tipejob+"%\' AND kota LIKE \'%"+namakota+"%\'"
        
        qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (tipe_job LIKE \'%"+searching+"%\' OR nama_perusahaan LIKE \'%"+searching+"%\')"
        results = RunSelect(qry)
        return render_template('advance.html', results = results, kota = kota, jenis = jenis)
    return render_template('advance.html', kota = kota, jenis = jenis) 