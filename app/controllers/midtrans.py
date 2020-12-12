from flask import Flask, render_template, request
from app import app

# Code di bawah sini
import midtransclient

# Create Snap API instance
snap = midtransclient.Snap(is_production=False,
                           server_key='SB-Mid-server-lPjI7VymABNAihCh157RTWHI',
                           client_key='SB-Mid-client-hH_K95RPUQyQl7L_')

# Build API parameter
param = {
    "transaction_details": {
        "order_id": "test-transaction-126",
        "gross_amount": 200000
    },
    "credit_card": {
        "secure": True
    },
    "customer_details": {
        "first_name": "budi",
        "last_name": "pratama",
        "email": "budi.pra@example.com",
        "phone": "08111222333"
    }
}

transaction = snap.create_transaction(param)
transaction_token = transaction['token']

@app.route('/midtrans')
def midtrans():
    return render_template('Midtrans.html', transaction=transaction_token)
