from flask import Flask, render_template, request, flash, session, redirect, url_for
from app import app, RunSelect, ExecuteCMD, saveApplyFilesLampiran
from datetime import timedelta

app.secret_key = "golekbarengkerjo"
app.permanent_session_lifetime = timedelta(weeks=12)


# Code di bawah sini
@app.route('/daftar', methods=["POST", "GET"])
def daftarpage():
    if "user" in session:
        return redirect(url_for('landingpage'))
    else:
        if request.method == "POST":
            session.permanent = True
            name = request.form["daftarname"].lower()
            email = request.form["daftaremail"].lower()
            password = request.form["daftarpassword"]
            confirmpassword = request.form["daftarconfirmpassword"]
            if name != "" and email != "" and password != "":
                if password == confirmpassword:
                    if len(password) > 7 and len(password) < 13:

                        qry = "SELECT email FROM pekerja"
                        results = RunSelect(qry)
                        for items in results:
                            if email == items[0]:
                                flash('Email telah digunakan')
                                return render_template('daftar.html')
                        qry = "SELECT * FROM pekerja"
                        data = RunSelect(qry)

                        qry = "CALL Pendaftaran(\'" + name + "\', \'" + email + "\', \'" + password + "\')"
                        ExecuteCMD(qry)

                        qry = "SELECT id_pekerja FROM pekerja WHERE email = \'" + email + "\'"
                        iid = RunSelect(qry)
                        session["user"] = name
                        session["iduser"] = iid[0][0]

                        sql = "SELECT foto_notification, kalimat_notification, id_lowongan FROM notification ORDER BY RAND() LIMIT 3"
                        hasil = RunSelect(sql)
                        session["notification"] = hasil

                        return redirect(url_for('landingpage'))
                    else:
                        flash('Password harus 8 - 12 karakter')
                        return render_template('daftar.html')
                else:
                    flash('Password dan Confirm Password berbeda')
                    return render_template('daftar.html')
            else:
                flash('Ada data yang tidak diisi')
                return render_template('daftar.html')
        else:
            return render_template('daftar.html')


@app.route('/masuk', methods=["POST", "GET"])
def masukpage():
    if "user" in session:
        return redirect(url_for('perusahaan'))
    else:
        session.permanent = True
        if request.method == "POST":
            email = request.form["masukemail"].lower()
            password = request.form["masukpassword"]
            qry = "SELECT nama_pekerja, email, password, id_pekerja, profil_pekerja FROM pekerja"
            results = RunSelect(qry)
            checker = False
            nama = None
            for items in results:
                if email == items[1] and password == items[2]:
                    checker = True
                    nama = items[0]
                    idpekerja = items[3]
                    profilpekerja = items[4]
                    break
            if checker == True:
                session.permanent = True
                session["email"] = email
                session["user"] = nama
                session["iduser"] = idpekerja
                session["profilepicture"] = profilpekerja

                sql = "SELECT foto_notification, kalimat_notification, id_lowongan FROM notification ORDER BY RAND() LIMIT 3"
                hasil = RunSelect(sql)
                session["notification"] = hasil
                # To Be Continued
                # To Be Continued
                # To Be Continued

                return redirect(url_for('landingpage'))
            # To Be Continued
            # To Be Continued
            # To Be Continued
            flash("Email atau Password Salah")
            return render_template('login.html')
        else:
            return render_template('login.html')


@app.route('/searchedlowongan/<idlowongan>', methods=["POST", "GET"])
def infolowongan(idlowongan):
    if request.method == "POST":
        if "user" in session:
            query = "SELECT perusahaan.id_perusahaan FROM perusahaan, jobs WHERE perusahaan.id_perusahaan = jobs.id_perusahaan AND id_jobs = \'" + idlowongan.upper(
            ) + "\';"
            results = RunSelect(query)

            files = request.files["applyfiles"]
            pekerjaid = session["iduser"]
            perusahaanid = results[0][0]            
            saveApplyFilesLampiran(files=files,
                                   pekerjaid=pekerjaid,
                                   perusahaanid=perusahaanid)
            return redirect(url_for('lowongan'))
        else:
            return redirect(url_for('masukpage'))
    else:
        query = "SELECT p.logo_perusahaan, j.tipe_job, j.duration_job, k.kota, j.minimum_gaji, j.maximum_gaji, p.website, p.email, p.telepon_perusahaan, j.kualifikasi_job, j.deskripsi_job FROM jobs j, perusahaan p, kota k WHERE j.id_perusahaan = p.id_perusahaan AND p.id_kota = k.id_kota AND j.id_jobs = \'" + idlowongan.upper(
        ) + "\';"
        results = RunSelect(query)

        return render_template('infolowongan.html',
                               logoperusahaan=results[0][0],
                               lowongantitle=results[0][1],
                               durationlowongan=results[0][2],
                               kota=results[0][3],
                               gajiminimum=results[0][4],
                               gajimaximum=results[0][5],
                               website=results[0][6],
                               email=results[0][7],
                               phone=results[0][8],
                               kualif=results[0][9].split(","),
                               desk=results[0][10].split(","))


@app.route('/searchedperusahaan/<idperusahaan>')
def infoperusahaan(idperusahaan):
    query = "SELECT p.foto_perusahaan, p.logo_perusahaan, p.deskripsi_perusahaan, p.website, p.email, p.telepon_perusahaan FROM perusahaan p WHERE p.id_perusahaan = \'" + idperusahaan + "\'"
    results = RunSelect(query)
    image = results[0][0]
    query = "SELECT p.logo_perusahaan, j.tipe_job, p.nama_perusahaan, k.kota, j.minimum_gaji FROM kota k, jobs j, perusahaan p WHERE p.id_perusahaan = j.id_perusahaan AND k.id_kota = p.id_kota AND p.id_perusahaan = \'" + idperusahaan + "\'"
    results2 = RunSelect(query)
    return render_template('InfoPerusahaan.html',
                           imageperusahaan=image,
                           logoperusahaan=results[0][1],
                           deskripsiperusahaan=results[0][2],
                           website=results[0][3],
                           email=results[0][4],
                           phone=results[0][5],
                           results=results2)


@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("email", None)
    session.pop("iduser", None)
    session.pop("profilepicture", None)
    return redirect(url_for('landingpage'))
    # return redirect(url_for('')) Landing Page
