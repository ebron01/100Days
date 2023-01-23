import requests

parameters = {
    "amount" : "10",
    "type" : "boolean",
    "category" : 18,
}

URL = "https://opentdb.com/api.php"
response = requests.get(URL, params=parameters)
response = response.json()
question_data = response["results"]
