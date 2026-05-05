from google import genai
from gemconnect import list_models
from gemconnect.connector import ask_gemini

client = genai.Client(api_key="YOUR API KEY")

result = ask_gemini("What is Python?", client, "gemini-2.5-flash")
print(result)
# list_models(client)
