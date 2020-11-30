from flask import Flask, render_template, request, flash, session
from app import app, RunSelect, ExecuteCMD
from datetime import timedelta

app.secret_key = "golekbarengkerjo"
app.permanent_session_lifetime = timedelta(weeks=12)
# Code di bawah sini
@app.route('/daftar', methods=["POST", "GET"])
def daftarpage():
    if "user" in session:
        return "Selamat anda telah login ternyata " + session["user"]
    else:

        if request.method == "POST":
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
                                return render_template('Daftar.html')
                        qry = "SELECT * FROM pekerja"
                        data = RunSelect(qry)
                        
                        if len(data) < 9:
                            iid = 'P000' + str(len(data) + 1)
                        elif len(data) < 99:
                            iid = 'P00' + str(len(data) + 1)
                        elif len(data) < 999:
                            iid = 'P0' + str(len(data) + 1)
                        else:
                            iid = 'P' + str(len(data) + 1)
                        
                        qry = "CALL Pendaftaran(\'"+ iid +"\', \'"+ name +"\', \'"+ email +"\', \'"+ password +"\')"
                        ExecuteCMD(qry)
                        return "Selamat anda telah mendaftar " + name
                    else:
                        flash('Password harus 8 - 12 karakter')
                        return render_template('Daftar.html')
                else:
                    flash('Password dan Confirm Password berbeda')
                    return render_template('Daftar.html')
            else:
                flash('Ada data yang tidak diisi')
                return render_template('Daftar.html')
        else:
            return render_template('Daftar.html')

@app.route('/masuk', methods=["POST", "GET"])
def masukpage():
    if "user" in session:
        # To Be Continued
        return "Selamat anda telah login " + session["user"]
    else:
        if request.method == "POST":
            email = request.form["masukemail"].lower()
            password = request.form["masukpassword"]
            qry = "SELECT nama_pekerja, email, password FROM pekerja"
            results = RunSelect(qry)
            checker = False
            nama = None
            for items in results:
                if email == items[1] and password == items[2]:
                    checker = True
                    nama = items[0]
                    break
            if checker == True:
                session.permanent = True
                session["email"] = email
                session["user"] = nama
                return "Anda telah login" + session["nama"]



            return "Yes"
        else:
            return render_template('Login.html')

#TestingCommitBranch