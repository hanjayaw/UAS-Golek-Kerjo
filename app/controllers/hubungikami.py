from flask import Flask, render_template, request,flash
from app import app, ExecuteCMD, RunSelect, RunSelectOne

# Code di bawah sini

@app.route('/hubungikami' ,methods=["POST","GET"])
def hubungi():

     sql = ("SELECT `id_jenis_masalah`,`jenis_masalah` FROM jenismasalah")
     masalah = RunSelect(sql)


     if request.method == "POST":
         nama = request.form["namacust"].upper()
         email = request.form["emailcust"]
         jenismasalah = request.form.get("jenismasalah")
         isimasalah = request.form["isimasalah"]

         if nama != "" and email != "" and isimasalah != "":
             qry = "CALL insertcustservice (\'" + email + "\', \'" + jenismasalah + "\', \'" + isimasalah + "\')"
             ExecuteCMD(qry)
             return render_template("contact.html",masalah = masalah)
         else:
             return render_template("contact.html",masalah = masalah , nama = nama, email= email, isitext= isitext) 
     else:
         return render_template("contact.html",masalah = masalah)
