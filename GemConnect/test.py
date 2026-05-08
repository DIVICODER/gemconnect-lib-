from google import genai
from gemconnect import list_models
from gemconnect.connector import ask_gemini
from gemconnect.errors import error_simplify

client = genai.Client(api_key="YOUR API KEY HERE")

result = ask_gemini("What is Python?", client, "gemini-2.5-flash-lite")
print(result)
print(ask_gemini("", client, "gemini-2.5-flash"))
print(ask_gemini(None, client, "gemini-2.5-flash"))
print(ask_gemini("hello", None, "gemini-2.5-flash"))

# # Test direct keywords
# print(error_simplify('TemplateNotFound'))
# print(error_simplify('429 Too Many Requests'))
# print(error_simplify('503 UNAVAILABLE'))

# # Test synonyms layer
# print(error_simplify('permission denied'))
# print(error_simplify('cors error occurred'))
# print(error_simplify('service unavailable'))

# # Test fallback
# print(error_simplify('some completely unknown error xyz'))
# # list_models(client)