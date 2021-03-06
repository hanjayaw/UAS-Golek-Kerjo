#https://zonacoding.com/article/penerapan-mvc-di-flask-python

from flask import Flask, url_for, session, make_response  ## import Flask dari package flask
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
from datetime import datetime
import os

app = Flask(__name__)
app.debug = True
mysql = MySQL()
mysql.init_app(app)

UPLOAD_FOLDER = os.path.join(app.root_path, 'static/filelampiran/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPLOAD_PROFILE = os.path.join(app.root_path, 'static/profile/')
app.config['UPLOAD_PROFILE'] = UPLOAD_PROFILE
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'pdf', 'docx', 'doc'}

app.config['MYSQL_DATABASE_HOST'] = 'golekkerjo.cmmunxguhntd.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'admingk'
app.config['MYSQL_DATABASE_PASSWORD'] = 'golekkerjo'
app.config['MYSQL_DATABASE_DB'] = 'db_isb19_001'

# app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'new_schema'

conn = cursor = None


def OpenDB():
    global conn, cursor
    conn = mysql.connect()
    cursor = conn.cursor()


def RunSelect(cmd):
    try:
        global cursor
        OpenDB()
        cursor.execute(cmd)
        res = cursor.fetchall()
        CloseDB()
    except:
        res = RunSelectSecond(cmd)
    return res


def RunSelectSecond(cmd):
    try:
        global cursor
        OpenDB()
        cursor.execute(cmd)
        res = cursor.fetchall()
        CloseDB()
    except:
        res = RunSelect(cmd)
    return res


def RunSelectOne(cmd):
    global cursor
    OpenDB()
    cursor.execute(cmd)
    res = cursor.fetchone()
    CloseDB()
    return res


def ExecuteCMD(cmd):
    global conn, cursor
    OpenDB()
    cursor.execute(cmd)
    conn.commit()
    CloseDB()


def CloseDB():
    global conn, cursor
    cursor.close()
    conn.close()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def saveApplyFilesLampiran(files, pekerjaid, perusahaanid):
    global conn, cursor
    if files and allowed_file(files.filename):
        query = "SELECT * FROM pekerjatoperusahaan"
        data = RunSelect(query)

        iid = 'PR' + str(len(data) + 1)

        pkp = iid
        query = "CALL InsertPKP (\'" + perusahaanid + "\', \'" + pekerjaid + "\', \'" + datetime.today(
        ).strftime('%Y-%m-%d') + "\')"
        ExecuteCMD(query)

        query = "SELECT * FROM lampiranpekerja"
        data = RunSelect(query)

        iid = 'LP' + str(len(data) + 1)

        extension = files.filename.split(".")

        filename = pkp + iid
        full = filename + '.' + extension[1]
        files.save(os.path.join(app.config['UPLOAD_FOLDER'], full))
        query = "CALL InsertLampiran(\'" + pkp + "\', \'" + full + "\')"
        ExecuteCMD(query)


def saveKTP(ktp):
    global conn, cursor
    if ktp and allowed_file(ktp.filename):
        qry = 'SELECT `id_pekerja` from pekerja WHERE id_pekerja = \'' + session[
            "iduser"].upper() + '\';'
        nama = RunSelect(qry)
        ext = ktp.filename.split(".")
        filename = "KTP" + nama[0][0] + '.' + ext[1]
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        except:
            None
        qry = 'CALL updatektp( \'' + filename + '\' , \'' + session[
            "iduser"].upper() + '\')'
        ExecuteCMD(qry)
        ktp.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


def saveProfil(profil):
    global conn, cursor
    if profil and allowed_file(profil.filename):
        qry = 'SELECT `id_pekerja`, `profil_pekerja` from pekerja WHERE id_pekerja = \'' + session[
            "iduser"].upper() + '\';'
        nama = RunSelect(qry)
        ext = profil.filename.split(".")
        filesebelum = nama[0][1]
        filename = "profil" + nama[0][0] + '.' + ext[1]
        try:
            os.remove(os.path.join(app.config['UPLOAD_PROFILE'], filesebelum))
        except:
            None

        session["profilepicture"] = filename
        qry = 'CALL updatefotoprofil (\'' + filename + '\'  , \'' + session[
            "iduser"].upper() + '\')'
        ExecuteCMD(qry)
        profil.save(os.path.join(app.config['UPLOAD_PROFILE'], filename))


def delcookie():
    res = make_response('Cookie Removed')
    res.set_cookie('foo', 'bar', max_age=0)


from app.controllers import *
