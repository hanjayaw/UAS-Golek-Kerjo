from flask import Flask, render_template, request, session, redirect, url_for
from app import app, ExecuteCMD, RunSelect, RunSelectOne, saveProfil, saveKTP
import math
app.secret_key = 'Golekbarangkerjo'

# Code di bawah sini


def before_request():
    app.jinja_env.cache = {}


@app.route('/profile', methods=["POST", "GET"])
def profile():
    if "user" in session:
        sqlutama = "SELECT `nama_pekerja`,`jenis_kelamin`,`umur_pekerja`,`pendidikan_terakhir`,`alamat`,`kota`,`provinsi`,`telepon_pekerja`,`email`,`instagram`,`linkedin`,`tipe_pekerjaan`,`durasi_pekerjaan`,`preferensi_gaji`,`ktp`FROM pekerja,kota,provinsi WHERE pekerja.id_kota = kota.id_kota and pekerja.id_provinsi = provinsi.id_provinsi and id_pekerja = \'"+ session["iduser"].upper() + "\';"
        return sqlutama
        pekerja = RunSelect(sqlutama)
        sql = ("SELECT `kota`,`id_kota` FROM kota")
        kota = RunSelect(sql)
        sql = ("SELECT `provinsi`, `id_provinsi` FROM provinsi")
        provinsi = RunSelect(sql)
        sql = ("SELECT `tipe_job` AS TIPE FROM jobs GROUP BY TIPE")
        jobs = RunSelect(sql)
        ktp = None
        durationpekerjaan = ['Full Time', 'Part Time', 'Freelance']
        lulusanutama = ['S1', 'S2', 'SMA']
        genderutama = ['Perempuan','Laki-laki']
        sqlhistori = ("SELECT `nama_perusahaan` , `nama_pekerja` , `tanggal_upload` FROM pekerjatoperusahaan pj ,pekerja,perusahaan WHERE pj.id_pekerja = pekerja.id_pekerja and pj.id_perusahaan = perusahaan.id_perusahaan and pj.id_pekerja = \'"
            + session["iduser"].upper() + "\';")
        histori = RunSelect(sqlhistori)


        if request.method == "POST":
            try:
                profil = request.files["applyprofil"]
            except:
                profil = None
            if profil:
                saveProfil(profil)
                pekerja = RunSelect(sqlutama)
                return redirect(request.url)
                app.before_request(before_request)                
            nama = request.form["namaprofil"].upper()
            gender = request.form.get("genderprofil")
            umur = request.form["umur"]
            lulusan = request.form.get("lulusan")
            alamat = request.form["alamatprofil"]
            kotanya = request.form.get("kota")
            provinsinya = request.form.get("provinsi")
            notelp = request.form["nomortelpon"]
            instagram = request.form["instagram"]
            linkedin = request.form["linkedin"]
            email = request.form["email"]
            try:
                ktp = request.files.get('applyktp', None)
            except:
                ktp = None
            jobnya = request.form.get("job")
            tipejob = request.form.get("tipejob")
            gaji = request.form["gaji"]

            #qry = 'UPDATE pekerja set '
            if nama != "" and nama != None:
                session["user"] = nama
                qry = 'CALL updatenama (\'' + nama + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)

            if gender != "" and gender != None:
                qry = 'CALL updatejeniskelamin (\'' + gender + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)

            if umur != "" and umur != None:
                qry = 'CALL updateumur (\'' + umur + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)

            if lulusan != "" and lulusan != None:
                #qry += ", pendidikan_terakhir = \'" + lulusan + "\'"
                qry = 'CALL updatelulusan (\'' + lulusan + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)


            if alamat != "" and alamat != None:

                #qry += ", alamat = \'" + alamat + "\'"
                qry = 'CALL updatealamat(\'' + alamat + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)


            if kotanya != "" and kotanya != None:

                #qry += ", id_kota = \'" + kotanya + "\'"
                qry = 'CALL updatekota(\'' + kotanya + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)

                


            if provinsinya != "" and provinsinya != None:

                #qry += ", id_provinsi = \'" + provinsinya + "\'"
                qry = 'CALL updateprovinsi(\'' + provinsinya + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)


            if notelp != "" and notelp != None:

                #qry += ", telepon_pekerja = \'" + notelp + "\'"
                qry = 'CALL updatetelepon(\'' + notelp + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)

            if instagram != "" and instagram != None:

                #qry += ", instagram = \'" + instagram + "\'"
                qry = 'CALL updateinstagram(\'' + instagram + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)
            if linkedin != "" and linkedin != None:
                #qry += ", linkedin = \'" + linkedin + "\'"
                qry = 'CALL updatelinkedin(\'' + linkedin + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)

            if email != "" and email != None:
                session["email"] = email
                qry = 'CALL updateemail(\'' + email + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)


            if ktp.filename != "" and ktp.filename != None:
                saveKTP(ktp)
            if jobnya != "" and jobnya != None:
                #qry += ", tipe_pekerjaan = \'" + jobnya + "\'"
                qry = 'CALL updatetipe(\'' + jobnya + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)


            if tipejob != "" and tipejob != None:
                #qry += ", durasi_pekerjaan = \'" + tipejob + "\'"
                qry = 'CALL updatedurasi(\'' + tipejob + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)


            if gaji != "" and gaji != None:
                #qry += ", preferensi_gaji = \'" + gaji + "\'"
                qry = 'CALL updategaji(\'' + gaji + '\'  , \'' + session["iduser"].upper() + '\')'
                ExecuteCMD(qry)


            #qry += 'WHERE id_pekerja = \'' + session["iduser"].upper() + '\';'
            #ExecuteCMD(qry)
            return render_template("profile.html",
                                   kota=kota,
                                   provinsi=provinsi,
                                   jobs=jobs,
                                   duration=durationpekerjaan,
                                   lulusannya=lulusanutama,
                                   genderkerja = genderutama,
                                   histori = histori,
                                   namapekerja=pekerja[0][0],
                                   genderpekerja=pekerja[0][1],
                                   umurpekerja=pekerja[0][2],
                                   lulusanpekerja=pekerja[0][3],
                                   alamatpekerja=pekerja[0][4],
                                   kota1=pekerja[0][5],
                                   provinsi1=pekerja[0][6],
                                   teleponpekerja=pekerja[0][7],
                                   emailpekerja=pekerja[0][8],
                                   instagrampekerja=pekerja[0][9],
                                   linkedinpekerja=pekerja[0][10],
                                   tipepekerja=pekerja[0][11],
                                   durasi=pekerja[0][12],
                                   gajipekerja=pekerja[0][13],
                                   ktpfoto=pekerja[0][14])
        else:
            return render_template("profile.html",
                                   kota=kota,
                                   provinsi=provinsi,
                                   jobs=jobs,
                                   duration=durationpekerjaan,
                                   lulusannya=lulusanutama,
                                   genderkerja = genderutama,
                                   histori = histori,
                                   namapekerja=pekerja[0][0],
                                   genderpekerja=pekerja[0][1],
                                   umurpekerja=pekerja[0][2],
                                   lulusanpekerja=pekerja[0][3],
                                   alamatpekerja=pekerja[0][4],
                                   kota1=pekerja[0][5],
                                   provinsi1=pekerja[0][6],
                                   teleponpekerja=pekerja[0][7],
                                   emailpekerja=pekerja[0][8],
                                   instagrampekerja=pekerja[0][9],
                                   linkedinpekerja=pekerja[0][10],
                                   tipepekerja=pekerja[0][11],
                                   durasi=pekerja[0][12],
                                   gajipekerja=pekerja[0][13],
                                   ktpfoto=pekerja[0][14])
    else:
        return redirect(url_for('masukpage'))