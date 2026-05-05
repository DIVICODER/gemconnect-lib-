'''
scary errors=> string

if you find anyof the key from the dict in the string.
then return the values.

we use dictory to store the key and value pair.
'''
keyword={
    
    ### Package setup - happening before anything
    'FutureWarning':'Your Gemini package is outdated. so, try to update to new package.',
   
    ### Flask setup - server not starting
    'ERR_CONNECTION_REFUSED':'Flask is not running.check for the app.run() properly.',
    'TemplateNotFound':'Flask cannot find your HTML file. Make sure your folder is named exactly templates.',
    'jinja2':'Error in your HTML template. Check your index.html file for mistakes.',
    
    ### API Key - authentication fails 
    'invalid api key':'Your API key is wrong...',
    'API key not found':'please enter a valid API key, as its missing or invalid.',
    '401 Unauthorized':'Unauthorized- check whether the credentials is valid,check whether the url is misconfiguration or invlid/expired tokens.',

    ### Quota and model - api call rejected
    'RESOURCE_EXHAUSTED':'Your project quota is exhausted. Create a brand new project at aistudio.google.com/apikey.',
    '429 Too Many Requests':'Too many request sent, so wait for a short duration before retrying as the model has no free tier now.',
    'limit: 0':'This model has no free quota. Check ai.dev/rate-limit and pick a model with quota available.',
    '403 Forbidden':'Your account cannot access this model you dont have permission to it.',
    '404 models':'Model not found.run package.list_models() to see whats available.',
    '413':'Your prompt is too long for Gemini.',
    '408':'Your request took too long, check your internet.',
    '422':'Request structure is incorrect.',

    ### Gemini server errors - gemini side mistake
    '500':'Gemini had an unexpected crash internal error.',
    '502':'Gemini servers not communicating. Try doing clear browser cache, refresh the page, wait for few minutes.',
    '503 UNAVAILABLE':'Too many people using it at the same time, so Wait a few minutes and try again.',
    '504 Timeout':'Gemini took long to respond. try again.',

    ### Safety - prompt blocked     
    'safety filters':'Gemini blocked this prompt due to safety policy. Try rephrasing your input.',
        
    ### Frontend - response display fails
    'blocked by CORS policy':'Even thought the frontend and backend both are localhost, but they have different ports so better use CORP(app) to overcome this problem.',
    'SyntaxError: Unexpected token':'The Flask server crashed and sent an "Internal Server Error" webpage instead of JSON, So better check the in Terminal for python crash.',
    '400 Bad Request':'You havent sent data in the format of Gemini wants so check it in the JSON.stringify() matches with keyname in request.json in flask.'
}

def error_simplify(s):
    s = s.lower() 
    output=''
    for k in keyword:
        if k.lower() in s:
            output=keyword[k]
            break
  

    if output=='':
        return "this error we dont know"
    return output

# ##Test 1 → 
# print(error_simplify('jinja2.exceptions.TemplateNotFound: index.html'))
# ##Test 2 → 
# print(error_simplify('TemplateNotFound: index.html'))
# ##Test 3 → add this new test yourself:

# print(error_simplify('jinja2 error occurred'))
# print(error_simplify('some random unknown error'))
    
# # Test every keyword you have
# print(error_simplify('429 Too Many Requests quota exceeded'))
# print(error_simplify('RESOURCE_EXHAUSTED limit: 0'))
# print(error_simplify('401 Unauthorized invalid credentials'))
# print(error_simplify('blocked by CORS policy'))
# print(error_simplify('404 models gemini not found'))
# print(error_simplify('FutureWarning google.generativeai'))
# print(error_simplify('some unknown error'))