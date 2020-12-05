from flask import Flask, render_template, request
from app import app, ExecuteCMD, RunSelect, RunSelectOne
import math
app.secret_key = 'Golekbarangkerjo'

# Code di bawah sini

@app.route('/profile', methods= ["POST","GET"])
def profile():
    sql= ("SELECT `kota`,`id_kota` FROM kota")
    kota = RunSelect(sql)
    sql=("SELECT `provinsi`, `id_provinsi` FROM provinsi")
    provinsi=RunSelect(sql)
    sql=("SELECT `tipe_job`, `id_jobs` FROM jobs")
    jobs= RunSelect(sql)


    if request.method == "POST":
        return "yes"
        nama = request.form["namaprofil"].upper()
        profil= request.files["applyprofil"]
        gender = request.form["genderprofil"]
        umur = request.form["umur"]
        lulusan = request.form.get("lulusan")
        alamat = request.form["alamatprofil"]
        kota = request.form.get("kota")
        provinsi =request.form.get("provinsi")
        notelp = request.form["nomortelepon"]
        instagram = request.form["instagram"]
        linkedin = request.form["linkedin"]
        email = request.form["email"]
        ktp = request.files["applyktp"]
        job =request.form.get("job")
        tipejob = request.form.get("tipejob")
        gaji = request.form["gaji"]
        if nama != "":
            qry= 'UPDATE pekerja set nama_pekerja = \''+ nama +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if profil.filename !="":
            qry= 'UPDATE pekerja set profil_pekerja = \''+ profil +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if gender != "":
            qry= 'UPDATE pekerja set jenis_kelamin= \''+ gender +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if umur != "":
            qry= 'UPDATE pekerja set umur = \''+ umur +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if lulusan != "":
            qry= 'UPDATE pekerja set pendidikan_terakhir = \''+ umur +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if alamat != "":
            qry= 'UPDATE pekerja set alamat = \''+ alamat +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if kota != "":
            qry= 'UPDATE pekerja set id_kota = \''+ kota +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if provinsi != "":
            qry= 'UPDATE pekerja set id_provinsi = \''+ provinsi +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if notelp != "":
            qry= 'UPDATE pekerja set telepon_pekerja = \''+ provinsi +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if instagram != "":
            qry= 'UPDATE pekerja set instagram = \''+ instagram +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if linkedin != "":
            qry= 'UPDATE pekerja set linkedin = \''+ linkedin +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)
        if ktp.filename != "":
            qry= 'UPDATE pekerja set ktp = \''+ ktp +'\' WHERE id_pekerja = \'' + iduser.upper(
            ) + '\';'
            ExecuteCMD(qry)      
    else :
        return render_template("profile.html", kota=kota, provinsi=provinsi, jobs=jobs)








    




