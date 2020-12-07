from flask import Flask, render_template, request, session, redirect, url_for
from app import app, ExecuteCMD, RunSelect, RunSelectOne, saveProfil, saveKTP
import math
app.secret_key = 'Golekbarangkerjo'

# Code di bawah sini

@app.route('/profile', methods= ["POST","GET"])
def profile():
    if "user" in session:        
        sqlutama = ("SELECT `nama_pekerja`,`jenis_kelamin`,`umur_pekerja`,`pendidikan_terakhir`,`alamat`,`kota`,`provinsi`,`telepon_pekerja`,`email`,`instagram`,`linkedin`,`tipe_pekerjaan`,`durasi_pekerjaan`,`preferensi_gaji`,`ktp`FROM pekerja,kota,provinsi WHERE pekerja.id_kota = kota.id_kota and pekerja.id_provinsi = provinsi.id_provinsi and id_pekerja = \'"+session["iduser"].upper(
            ) + "\';")
        pekerja = RunSelect(sqlutama)
        sql= ("SELECT `kota`,`id_kota` FROM kota")
        kota = RunSelect(sql)
        sql=("SELECT `provinsi`, `id_provinsi` FROM provinsi")
        provinsi=RunSelect(sql)
        sql=("SELECT `tipe_job` AS TIPE FROM jobs GROUP BY TIPE")
        jobs= RunSelect(sql)    
        ktp = None
        durationpekerjaan = ['Full Time', 'Part Time', 'Freelance'] 
        lulusanutama = ['S1','S2','SMA']   

        if request.method == "POST":
            try:
                profil= request.files["applyprofil"]
            except:
                profil = None
            if profil:
                saveProfil(profil)
                pekerja = RunSelect(sqlutama)
                return render_template("profile.html", kota=kota, provinsi=provinsi, jobs=jobs, duration = durationpekerjaan, lulusannya = lulusanutama,
                namapekerja= pekerja[0][0],
                genderpekerja= pekerja[0][1],
                umurpekerja= pekerja[0][2],
                lulusanpekerja = pekerja[0][3],
                alamatpekerja = pekerja[0][4],
                kota1 = pekerja[0][5],
                provinsi1= pekerja[0][6],
                teleponpekerja = pekerja[0][7],
                emailpekerja= pekerja[0][8],
                instagrampekerja = pekerja[0][9],
                linkedinpekerja= pekerja[0][10],
                tipepekerja = pekerja[0][11],
                durasi = pekerja[0][12],
                gajipekerja = pekerja[0][13],
                ktpfoto = pekerja[0][14]
                )
            nama = request.form["namaprofil"].upper()
            gender = request.form["genderprofil"]
            umur = request.form["umur"]
            lulusan = request.form.get("lulusan")
            alamat = request.form["alamatprofil"]
            kotanya = request.form.get("kota")
            provinsinya =request.form.get("provinsi")
            notelp = request.form["nomortelpon"]
            instagram = request.form["instagram"]
            linkedin = request.form["linkedin"]
            email = request.form["email"]
            try:
                ktp = request.files.get('applyktp', None)
            except:
                ktp = None
            jobnya =request.form.get("job")
            tipejob = request.form.get("tipejob")
            gaji = request.form["gaji"]
            if nama != "":
                session["user"]= nama
                qry= 'UPDATE pekerja set nama_pekerja = \''+ nama +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if gender != "":
                qry= 'UPDATE pekerja set jenis_kelamin= \''+ gender +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if umur != "":
                qry= 'UPDATE pekerja set umur_pekerja = \''+ umur +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if lulusan != "":
                qry= 'UPDATE pekerja set pendidikan_terakhir = \''+ lulusan +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if alamat != "":
                qry= 'UPDATE pekerja set alamat = \''+ alamat +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if kotanya != "":
                qry= 'UPDATE pekerja set id_kota = \''+ kotanya +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if provinsinya != "":
                qry= 'UPDATE pekerja set id_provinsi = \''+ provinsinya +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if notelp != "":
                qry= 'UPDATE pekerja set telepon_pekerja = \''+ notelp +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if instagram != "":
                qry= 'UPDATE pekerja set instagram = \''+ instagram +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if linkedin != "":
                qry= 'UPDATE pekerja set linkedin = \''+ linkedin +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if ktp.filename != "":
                saveKTP(ktp)
            if jobnya != "":
                qry= 'UPDATE pekerja set tipe_pekerjaan = \''+ jobnya +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if tipejob != "":
                qry= 'UPDATE pekerja set durasi_pekerjaan = \''+ tipejob +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry)
            if gaji != "":
                qry= 'UPDATE pekerja set preferensi_gaji = \''+ gaji +'\' WHERE id_pekerja = \'' + session["iduser"].upper(
                ) + '\';'
                ExecuteCMD(qry) 
            pekerja = RunSelect(sqlutama)
            return render_template("profile.html", kota=kota, provinsi=provinsi, jobs=jobs,duration = durationpekerjaan, lulusannya = lulusanutama,
                namapekerja= pekerja[0][0],
                genderpekerja= pekerja[0][1],
                umurpekerja= pekerja[0][2],
                lulusanpekerja = pekerja[0][3],
                alamatpekerja = pekerja[0][4],
                kota1 = pekerja[0][5],
                provinsi1= pekerja[0][6],
                teleponpekerja = pekerja[0][7],
                emailpekerja= pekerja[0][8],
                instagrampekerja = pekerja[0][9],
                linkedinpekerja= pekerja[0][10],
                tipepekerja = pekerja[0][11],
                durasi = pekerja[0][12],
                gajipekerja = pekerja[0][13],
                ktpfoto= pekerja[0][14]
                )     
        else :
            
            return render_template("profile.html", kota=kota, provinsi=provinsi, jobs=jobs,duration = durationpekerjaan, lulusannya = lulusanutama,
                namapekerja= pekerja[0][0],
                genderpekerja= pekerja[0][1],
                umurpekerja= pekerja[0][2],
                lulusanpekerja = pekerja[0][3],
                alamatpekerja = pekerja[0][4],
                kota1 = pekerja[0][5],
                provinsi1= pekerja[0][6],
                teleponpekerja = pekerja[0][7],
                emailpekerja= pekerja[0][8],
                instagrampekerja = pekerja[0][9],
                linkedinpekerja= pekerja[0][10],
                tipepekerja = pekerja[0][11],
                durasi = pekerja[0][12],
                gajipekerja = pekerja[0][13],
                ktpfoto = pekerja[0][14]
                )
    else:
        return redirect(url_for('masukpage'))