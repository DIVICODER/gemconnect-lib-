'''
scary errors=> string

if you find anyof the key from the dict in the string.
then return the values.

we use dictory to store the key and value pair.
'''
keyword = {

    ### Package setup
    'FutureWarning':
        "Your Gemini package is old. Open your terminal and run: pip install --upgrade google-generativeai",

    ### Flask setup
    'ERR_CONNECTION_REFUSED':
        "Your Flask server is not running. Go to your terminal and run your app.py file first, then try again.",

    'TemplateNotFound':
        "Flask cannot find your HTML file. Make sure your HTML file is inside a folder named exactly 'templates' (no capital letters, no spaces).",

    'jinja2':
        "There is a mistake inside your HTML file. Open index.html and look for any {{ }} or {% %} blocks — one of them has a typo.",

    ### API Key
    'invalid api key':
        "Your API key is wrong. Go to aistudio.google.com/apikey, copy your key again and paste it carefully — even one wrong character breaks it.",

    'API key not found':
        "You forgot to add your API key. Go to aistudio.google.com/apikey, copy your key and paste it where the client is set up in your code.",

    '401 Unauthorized':
        "Gemini does not recognize you. Your API key is either wrong, expired, or missing. Go to aistudio.google.com/apikey and get a fresh one.",

    ### Quota and model
     'limit: 0':
        "This Gemini model has no free quota left. Run list_models() to see other models or go to ai.dev/rate-limit to find one with free quota.",

    'RESOURCE_EXHAUSTED':
        "You have used up all your free Gemini quota. Go to aistudio.google.com/apikey, create a brand new project and generate a new API key from there.",

    '429 Too Many Requests':
        "You sent too many requests too fast. Wait 30-60 seconds and try again.",

    '403 Forbidden':
        "Your account does not have permission to use this model. Try a different model like 'gemini-2.0-flash' which is free for everyone.",

    '404 models':
        "The model name you typed does not exist. Run list_models() to see the exact names and copy-paste one of those.",

    ### Gemini server errors
    'InternalServerError':
        "Something crashed on Gemini's side — this is not your fault. Wait a minute and try the exact same request again.",

    '502':
        "Gemini's servers are not communicating right now. Wait 2-3 minutes and try again.",

    '503 UNAVAILABLE':
        "Too many people are using Gemini right now. Wait a few minutes and try again.",

    '504 Timeout':
        "Gemini took too long to reply. Wait a moment and try again.",

    ### Request errors
    'PayloadTooLarge':
        "Your prompt is too long. Try splitting it into smaller pieces and sending one part at a time.",

    'DeadlineExceeded':
        "Your request took too long. Check your internet connection and try again.",

    'UnprocessableEntity':
        "Gemini did not understand how your request was structured. Make sure you are passing the prompt as a plain string and not inside a list or dict.",

    ### Safety
    'safety filters':
        "Gemini blocked your prompt because it triggered its safety rules. Try rewriting your question in a more neutral way.",

    ### Frontend
    'blocked by CORS policy':
        "Your browser is blocking the request because your frontend and backend are on different ports. Install flask-cors and add CORS(app) to your Flask file.",

    'SyntaxError: Unexpected token':
        "Your Flask server crashed and sent back an error page instead of data. Check your terminal — the real error is printed there.",

    '400 Bad Request':
        "The data you sent does not match what Flask expected. Make sure the key name in your JavaScript fetch matches exactly what you use in request.json in Flask.",
    
    'invalid api key':
         "Your API key is wrong. Go to aistudio.google.com/apikey, copy your key again and paste it carefully — even one wrong character breaks it.",

    ### Install errors
    'ModuleNotFoundError':
        "A required package is not installed. Open your terminal and run: pip install google-generativeai",

    'No module named':
        "A required package is not installed. Open your terminal and run: pip install google-generativeai",

    ### Network errors
    'ConnectionError':
        "Could not reach Gemini. Check your internet connection and try again.",

    'SSLError':
        "A secure connection to Gemini failed. Check your internet or try a different network.",

    'NewConnectionError':
        "No internet connection found. Make sure you are connected to the internet and try again.",
}


synonyms = {
    # Quota
    'quota':               'RESOURCE_EXHAUSTED',
    'exhausted':           'RESOURCE_EXHAUSTED',
    'resource exhausted':  'RESOURCE_EXHAUSTED',

    # Rate limit
    'rate limit':          '429 Too Many Requests',
    'too many':            '429 Too Many Requests',

    # Permission
    'permission denied':   '403 Forbidden',
    'PERMISSIO DENIED':    '403 Forbidden',
    'access denied':       '403 Forbidden',
    'forbidden':           '403 Forbidden',

    # Model
    'model not found':     '404 models',
    'not_found':           '404 models',

    # Timeout
    'timeout':             '504 Timeout',
    'timed out':           '504 Timeout',
    'deadline':            'DeadlineExceeded',

    # Payload
    'payload too large':   'PayloadTooLarge',
    'prompt too long':     'PayloadTooLarge',

    # Frontend
    'cors':                'blocked by CORS policy',
    'cross-origin':        'blocked by CORS policy',

    # Template
    'template':            'TemplateNotFound',

    # Safety
    'safety':              'safety filters',
    'blocked':             'safety filters',

    # Auth
    'invalid key':         'invalid api key',
    'API_KEY_INVALID':     'invalid api key',  
    'API key not valid':   'invalid api key',
    'unauthorized':        '401 Unauthorized',

    # Request
    'bad request':         '400 Bad Request',

    # Server
    'server error':        'InternalServerError',
    'internal error':      'InternalServerError',
    'bad gateway':         '502',
    'service unavailable': '503 UNAVAILABLE',

    # Connection
    'connection refused':  'ERR_CONNECTION_REFUSED',

    # Package
    'deprecated':          'FutureWarning',
    'outdated':            'FutureWarning',
}


def error_simplify(s):
    s_lower = s.lower()

    # Layer 1 — direct keyword match
    for k in keyword:
        if k.lower() in s_lower:
            return f"{keyword[k]} Raw error: {s}"

    # Layer 2 — synonym match
    for alias in synonyms:
       if alias.lower() in s_lower:    # ← add .lower() here
            mapped_key = synonyms[alias]
            return f"{keyword[mapped_key]} Raw error: {s}"
    # Nothing matched
    return f"GemConnect could not simplify this error. Here is the raw error for you to search online: {s}"