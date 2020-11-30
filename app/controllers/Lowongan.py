from flask import Flask, render_template, request
from app import app, ExecuteCMD, RunSelect, RunSelectOne
import math 






@app.route('/lowongan', methods = ["POST", "GET"])
def lowongan():
    currentpage = request.args.get('page',1) #langkah 1 tau currentpage
    sql = "SELECT COUNT(*) as jumlah_lowongan FROM jobs"
    res = RunSelectOne(sql) #LANGKAH KE 2 COUNT DATA 
    n_item = res[0] 
    n_size = 6
    n_pages = math.ceil(n_item/n_size)
    if int(currentpage) > 1:
        currentindex = int(currentpage) * n_size - n_size
    else:
        currentindex = 0  
    sql = "SELECT `tipe_job`, `minimum_gaji`, `nama_perusahaan` ,`kota`, `logo_perusahaan` from jobs j, kota k, perusahaan p where p.id_kota = k.id_kota and j.id_perusahaan = p.id_perusahaan limit 6"
    results = RunSelect(sql)
    sql = "SELECT `tipe_job`, `minimum_gaji`, `nama_perusahaan` ,`kota`, `logo_perusahaan` from jobs j, kota k, perusahaan p where p.id_kota = k.id_kota and j.id_perusahaan = p.id_perusahaan limit "+str(currentindex)+", " +str(n_size)+";"
    hasil = RunSelect(sql)
    return render_template('index.html',results = results, hasil = hasil, pages=n_pages, currentpage=int(currentpage))
# Code di bawah sini

@app.route('/tes')
def tes():
    return "halo"