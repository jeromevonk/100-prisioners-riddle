import requests

def get_random_sequence():
  url = "https://api.random.org/json-rpc/4/invoke"

  # Payload
  payload = {
  "id": 3097,
  "jsonrpc": "2.0",
  "method": "generateIntegers",
  "params": {
      "apiKey": "487bc633-c177-4da3-8a18-f123760623fc",
      "n": 100,
      "min": 0,
      "max": 99,  # easier to translate to 0-index
      "replacement": False,
      "base": 10,
      "pregeneratedRandomization": None
    }
  }
  response = requests.post(url, json=payload).json()

  return response["result"]["random"]["data"]