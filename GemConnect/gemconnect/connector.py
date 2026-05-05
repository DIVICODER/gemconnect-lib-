# connector.py

from .errors import error_simplify    # imports your errors file

def ask_gemini(prompt, client, model):

    ## checking if the prompt is text input only.
    if not isinstance(prompt, str):
            return "gemconnect v1.0 supports text prompts only. For image or audio pass directly to Gemini."
    try:

        # step 1 → call Gemini here
        response=client.models.generate_content(model=model,contents=prompt)
        
        # step 2 → return the result
        return response.text
        

    except Exception as e:
        # step 3 → pass error to error_simplify
        # print("RAW ERROR:", str(e))  
        return error_simplify(str(e))
        # step 4 → return friendly message
        