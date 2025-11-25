"""Week 8 exercise 5 Parsing"""

import requests # Import the tool to talk to the web
url = "https://official-joke-api.appspot.com/random_joke"
 # 1. Send the request
print("Calling the server...")
response = requests.get(url)
 # 2. Check the Status Code (200 = Success, 404 = Not Found)
print(f"Status Code: {response.status_code}")
 # 3. See the raw text data
print("Raw Data:")
if response.status_code == 200:
 # Convert raw text to a Python Dictionary
 joke_data = response.json()
 # Now extract the specific parts (Keys: 'setup' and 'punchline')
 setup = joke_data['setup']
 punchline = joke_data['punchline']
 print("----------------")
 print(f"Joke: {setup}")
 print(f"Answer: {punchline}")
 print("----------------")
else:
 print("Error: Could not fetch joke.")