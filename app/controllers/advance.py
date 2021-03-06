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
        querynya = ""
        if tipejobs != "":
            querynya = querynya +  " AND tipe_job LIKE \'%"+tipejobs+"%\'"
        if namakota != "":
            querynya = querynya + "  AND kota LIKE \'%"+namakota+"%\'"
        if jenisjobs != "":
            querynya = querynya + " AND duration_job LIKE \'%"+jenisjobs+"%\'"
        if gajimin != "":
            querynya = querynya + " AND minimum_gaji > \'"+gajimin+"\' - 1 "
        if gajimax != "":
            querynya = querynya + " AND minimum_gaji < \'"+gajimax+"\' + 1"
        if searching == "":
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan "+ querynya + ";"
            print(qry)
            # qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job LIKE \'%"+jenisjobs+"%\' AND tipe_job LIKE \'%"+tipejobs+"%\' AND kota LIKE \'%"+namakota+"%\' AND minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1"
        
        # elif searching == "" and jenisjobs == "" and tipejobs == "" and namakota == "" and gajimin != "" and gajimax != "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1"
        # elif searching == "" and jenisjobs == "" and tipejobs == "" and namakota != "" and gajimin == "" and gajimax == "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND kota LIKE \'%"+namakota+"%\'"
        # elif searching == "" and jenisjobs == "" and tipejobs != "" and namakota == "" and gajimin == "" and gajimax == "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND tipe_job LIKE \'%"+tipejobs+"%\'"
        # elif searching == "" and jenisjobs != "" and tipejobs == "" and namakota == "" and gajimin == "" and gajimax == "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job LIKE \'%"+jenisjobs+"%\'"
                
        # elif searching == "" and jenisjobs != "" and tipejobs != "" and namakota == "" and gajimin == "" and gajimax == "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job LIKE \'%"+jenisjobs+"%\' AND tipe_job LIKE \'%"+tipejobs+"%\'"
        # elif searching == "" and jenisjobs != "" and tipejobs == "" and namakota != "" and gajimin == "" and gajimax == "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job LIKE \'%"+jenisjobs+"%\' AND kota LIKE \'%"+namakota+"%\'"
        # elif searching == "" and jenisjobs != "" and tipejobs == "" and namakota == "" and gajimin != "" and gajimax != "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job LIKE \'%"+jenisjobs+"%\' AND minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1"
        
        # elif searching == "" and jenisjobs == "" and tipejobs != "" and namakota != "" and gajimin == "" and gajimax == "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND tipe_job LIKE \'%"+tipejobs+"%\' AND kota LIKE \'%"+namakota+"%\'"
        # elif searching == "" and jenisjobs == "" and tipejobs != "" and namakota == "" and gajimin != "" and gajimax != "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND tipe_job LIKE \'%"+tipejobs+"%\' AND minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1"
        
        # elif searching == "" and jenisjobs == "" and tipejobs == "" and namakota != "" and gajimin != "" and gajimax != "":
        #     qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND kota LIKE \'%"+namakota+"%\' AND minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1"
        

        
        elif searching != "" and jenisjobs == "" and tipejobs == "" and namakota == "" and gajimin == "" and gajimax == "":
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (tipe_job LIKE \'%"+searching+"%\' OR nama_perusahaan LIKE \'%"+searching+"%\')"
        
        else:
            # qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (UPPER(tipe_job) LIKE UPPER(\'%"+searching+"%\') OR UPPER(nama_perusahaan) LIKE UPPER(\'%"+searching+"%\')) AND (duration_job LIKE \'"+jenisjobs+"\' OR tipe_job LIKE \'"+tipejobs+"\' OR kota LIKE \'"+namakota+"\' OR minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1)"
            qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND (tipe_job LIKE \'%"+searching+"%\' OR nama_perusahaan LIKE \'%"+searching+"%\') AND (duration_job LIKE \'"+jenisjobs+"\' OR tipe_job LIKE \'"+tipejobs+"\' OR kota LIKE \'%"+namakota+"%\' AND minimum_gaji > \'"+gajimin+"\' - 1 AND minimum_gaji < \'"+gajimax+"\' + 1)"
        results = RunSelect(qry)
        return render_template('advance.html', results=results)
    return render_template('advance.html')


@app.route('/freelance')
def freelance():
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job = 'Freelance'"
    results = RunSelect(qry)

    mingaji = []
    for items in range(len(results)):
        mingaji.append(format(int(results[items][3]), ","))
    pr = len(results)
    return render_template('hasilcari.html',
                           results=results,
                           mingaji=mingaji,
                           pr=pr)


@app.route('/parttime')
def parttime():
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job = 'Part Time'"
    results = RunSelect(qry)
    mingaji = []
    for items in range(len(results)):
        mingaji.append(format(int(results[items][3]), ","))
    pr = len(results)
    return render_template('hasilcari.html',
                           results=results,
                           mingaji=mingaji,
                           pr=pr)


@app.route('/fulltime')
def fulltime():
    qrykota = "SELECT kota from kota ORDER BY kota"
    session["kota"] = RunSelect(qrykota)
    qryjenis = "SELECT tipe_job FROM jobs GROUP BY tipe_job"
    session["jenis"] = RunSelect(qryjenis)
    qry = "SELECT tipe_job , nama_perusahaan , kota , minimum_gaji , logo_perusahaan, id_jobs FROM jobs , perusahaan , kota WHERE perusahaan.id_kota = kota.id_kota AND jobs.id_perusahaan = perusahaan.id_perusahaan AND duration_job = 'Full Time'"
    results = RunSelect(qry)
    mingaji = []
    for items in range(len(results)):
        mingaji.append(format(int(results[items][3]), ","))
    pr = len(results)
    return render_template('hasilcari.html',
                           results=results,
                           mingaji=mingaji,
                           pr=pr)
