# connector.py

from .errors import error_simplify    # imports your errors file
def ask_gemini(prompt, client, model):

    # Check 1 — empty prompt

    if prompt is None:
        return "Your prompt is None. Please pass a text string like ask_gemini('hello', client, model)."
    
    if prompt.strip() == "":
        return "Your prompt is empty. Please type something before sending."

    # Check 2 — non-string prompt
    if not isinstance(prompt, str):
        return "Your prompt must be plain text. You passed a " + type(prompt).__name__ + " instead of a string."

    # Check 3 — client looks wrong

    if isinstance(client, str):
        return "You passed a string as the client. You need to create a proper Gemini client first using genai.Client(api_key=...)."

    if client is None:
        return "Your Gemini client is None. Make sure you created it using genai.Client(api_key=...) before calling ask_gemini()."
    if model is None:
        return "You forgot to pass a model name. Try ask_gemini(prompt, client, 'gemini-2.0-flash')."

    if not isinstance(model, str):
        return "Your model name must be a string like 'gemini-2.0-flash'. You passed a " + type(model).__name__ + " instead."

    if model.strip() == "":
        return "Your model name is empty. Try ask_gemini(prompt, client, 'gemini-2.0-flash')."

    # rest of your existing code...
    try:
        response = client.models.generate_content(model=model, contents=prompt)
        return response.text
    except Exception as e:
        return error_simplify(str(e))