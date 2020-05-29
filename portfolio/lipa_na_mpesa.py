import requests
  
    access_token = "Access-Token"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
      "InitiatorName": " ",
      "SecurityCredential":" ",
      "CommandID": " ",
      "Amount": " ",
      "PartyA": " ",
      "PartyB": " ",
      "Remarks": " ",
      "QueueTimeOutURL": "http://your_timeout_url",
      "ResultURL": "http://your_result_url",
      "Occasion": " "
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)


    