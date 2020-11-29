#https://zonacoding.com/article/penerapan-mvc-di-flask-python

from flask import Flask ## import Flask dari package flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_HOST'] = 'jmswijaya.com'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER']= 'isb19'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Isb@2019'
app.config['MYSQL_DATABASE_DB'] = 'db_isb19_001'

conn = cursor = None

def OpenDB():
    global conn, cursor
    conn = mysql.connect()
    cursor = conn.cursor()

def RunSelect(cmd):
    global cursor
    OpenDB()
    cursor.execute(cmd)
    res = cursor.fetchall()
    CloseDB()
    return res

def RunSelectOne(cmd):
    global cursor
    OpenDB()
    cursor.execute(cmd)
    res = cursor.fecthone()
    CloseDB()
    return res

def ExecuteCMD(cmd):
    global conn, cursor
    OpenDB()
    cursor.execute(cmd)
    conn.commit()
    res = cursor.rowCount()
    CloseDB()
    return res

def CloseDB():
    global conn, cursor
    cursor.close()
    conn.close()

from app.controllers import  *