from .connector import ask_gemini
__version__ = "1.0.0"

def list_models(client):
    print("The available Gemini Models are:")
    for model in client.models.list():
        print(model.name)

    
