import requests

url = "https://gatewaystaging.payscout.com/api/process"

payload = "client_username={yourUsername}&client_password={yourPassword}&client_token=token&processing_type=CAPTURE&currency=USD&initial_amount=99.99&original_transaction_id=A000133RY3R&billing_invoice_number=1999"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text) 
