import requests

url = "https://gatewaystaging.payscout.com/api/process"

payload = "client_username={yourUsername}&client_password={yourPassword}&client_token=token&processing_type=REFUND¤cy=USD&initial_amount=99.99&original_transaction_id=A0001FFCDJ9"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text) 
