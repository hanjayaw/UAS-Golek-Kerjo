from flask import Flask, render_template, request, session
from app import app, RunSelect
import midtransclient

# Code di bawah sini


@app.route('/premium', methods=["POST", "GET"])
def premium():    
    snap = midtransclient.Snap(is_production=False,
                            server_key='SB-Mid-server-lPjI7VymABNAihCh157RTWHI',
                            client_key='SB-Mid-client-hH_K95RPUQyQl7L_')

    # Build API parameter
    qry = "SELECT * FROM pemasukan"
    results = RunSelect(qry)
    inlength = len(results) + 1 #PEMASUKAN KE BERAPA
    fullorderid = "IN" + str(inlength) + session["iduser"]
    telepon = ("SELECT `telepon_pekerja` from pekerja WHERE id_pekerja = \'" + session["iduser"].upper() + "\';")
    notelepon = RunSelect(telepon)
    if notelepon[0][0] != "": 
        asu = notelepon[0][0]
    else:
        asu = "Tidak Diketahui "
    param = {
        "transaction_details": {
            "order_id": fullorderid, #DIUBAH DENGAN MAX PEMASUKAN + 1 (QUERY)
            "gross_amount": 50000
        },
        "credit_card": {
            "secure": True
        },
        "customer_details": {
            "first_name": session["user"],
            "last_name": "",
            "email": session["email"],
            "phone" : asu
            # "phone": "08111222333" #KALAU NOMOR HP NYA NGGA ADA DI PROFILE, GANTI JADI Tidak Diketahui (IF dan QUERY)
        },
        "callbacks": {
            "finish": "http://127.0.0.1:5000/keapproutemu" 
            #KE APP ROUTE BARU UNTUK MEMASUKKAN DATA KE TABEL PEMASUKAN 
            #HABIS ITU MENGUBAH STATUS PEKERJA DARI FREE KE PREMIUM
            #HABIS DARI APP ROUTE MU LANGSUNG KE PROFILE
                            
        }
    }

    transaction = snap.create_transaction(param)
    transaction_token = transaction['token']
    return render_template("pembayaran.html", transaction=transaction_token)

