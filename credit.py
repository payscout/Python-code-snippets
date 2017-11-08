import requests

url = "https://gatewaystaging.payscout.com/api/process"

payload = "client_username={yourUsername}&client_password={yourPassword}&client_token=token&processing_type=CREDIT&expiration_month=10&expiration_year=2022&account_number={yourTestCardNumber}&cvv2=123&currency=USD&initial_amount=99.99"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text) 
