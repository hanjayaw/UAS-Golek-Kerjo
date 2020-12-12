from flask import Flask, render_template, request, session, redirect, url_for
from app import app, ExecuteCMD, RunSelect, RunSelectOne

@app.route('/ksjadfljakjHJJLKJl46546544SFDGdasd')
def pembayaran():
    qry = "UPDATE `pekerja` set id_membership = 'MB01' WHERE id_pekerja =\'" + session["iduser"].upper() + "\';"
    ExecuteCMD(qry)
    return redirect(url_for('profile'))
