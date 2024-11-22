import requests
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Fetch a random cat fact
url = "https://catfact.ninja/fact"
response = requests.get(url)

# Ensure the API request was successful
if response.status_code == 200:
    # Extract the fact from the JSON response
    fact = response.json().get("fact", "No fact found")
    
    # Translate the fact into Indonesian
    translated_fact = translator.translate(fact, dest='id')
    
    # Print the original and translated facts
    print("Original Fact:", fact)
    print("Translated Fact (Indonesian):", translated_fact.text)
else:
    print(f"Error: Unable to fetch fact. Status code: {response.status_code}")
