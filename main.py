import requests
import os
#LIST OF API'S
# Google Sheet Data Management - https://sheety.co/
#
# Kiwi Partners Flight Search API (Free Signup, Credit Card not required) - https://partners.kiwi.com/
#
# Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
#
# Twilio SMS API - https://www.twilio.com/docs/sms

#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

SHEETY_ENDPOINT = "https://api.sheety.co/9812358a3e25c44b28f5bca7cf88eec1/flightDeals/prices"
BEARER = os.environ["BEARER_TOKEN"]

headers = {
    "Authorization": BEARER
}
sheet_inputs={
    "price": {
        "city": "TEST",
        "iataCode": "TEST",
        "lowestPrice": "99"
        }
}
sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=headers)
print(sheety_response.text)
