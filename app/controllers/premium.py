from flask import Flask, render_template, request, session
from app import app, RunSelect
import midtransclient

# Code di bawah sini


@app.route('/premium')
def premium():
        
    snap = midtransclient.Snap(is_production=False,
                            server_key='SB-Mid-server-lPjI7VymABNAihCh157RTWHI',
                            client_key='SB-Mid-client-hH_K95RPUQyQl7L_')

    # Build API parameter
    param = {
        "transaction_details": {
            "order_id": "IN1",
            "gross_amount": 50000
        },
        "credit_card": {
            "secure": True
        },
        "customer_details": {
            "first_name": session["user"],
            "last_name": "",
            "email": session["email"],
            "phone": "08111222333"
        }
    }

    transaction = snap.create_transaction(param)
    transaction_token = transaction['token']
    return render_template("pembayaran.html", transaction=transaction_token)