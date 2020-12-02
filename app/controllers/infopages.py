from flask import Flask, render_template, request
from app import app, RunSelect, ExecuteCMD


# Code di bawah sini
@app.route('/searched/<idlowongan>')
def infolowongan(idlowongan):
    query = "SELECT p.logo_perusahaan, j.tipe_job, j.duration_job, k.kota, j.minimum_gaji, j.maximum_gaji, p.website, p.email, p.telepon_perusahaan, j.kualifikasi_job, j.deskripsi_job FROM jobs j, perusahaan p, kota k WHERE j.id_perusahaan = p.id_perusahaan AND p.id_kota = k.id_kota AND j.id_jobs = \'" + idlowongan.upper() + "\';"
    results = RunSelect(query)

    return render_template('InfoLowongan.html',
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
