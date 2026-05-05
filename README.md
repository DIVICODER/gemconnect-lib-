# GemConnect

gemconnect sits between Flask and Gemini, calls the API safely, and if anything goes wrong, translates the scary technical error into a simple message the beginner can understand and fix.

---

## The Problem

As an engineer, it felt fascinating to connect upcoming trends like AI into a website and see it work. Getting Gemini to respond in the terminal felt exciting. But when I tried to connect it with the frontend, it once again felt like zero.

Errors kept coming when interconnecting the frontend with Flask. Initially I tried to debug on my own, but it reached a threshold where I shifted from being curious and excited to a mood of just finishing what I had started. I kept copy-pasting the error to an AI bot to debug. Sometimes it worked, sometimes it didn't. But whether it worked or not, I hadn't been able to debug the error myself.

The errors were in technical terms like "404" — like these types of numbers. And in some cases it would show a scary list of errors and say "JSON error" like that, making it difficult to understand what went wrong and where.

What I needed was an error document to understand each error. That problem led to the creation of this library.

---

## What GemConnect Does

GemConnect gets the scary error and then converts that to a human-understandable error for easy debugging.

```
WITHOUT GemConnect:
Flask → Gemini → 😵 Scary JSON error dump → Beginner gives up

WITH GemConnect:
Flask → GemConnect → Gemini → ❌ Error?
                                    ↓
                        "Hey! Your API key looks wrong.
                         Double check it here → GemBridge(api_key=...)"
```

This makes connecting to the AI service, like a PDF to text extraction, feel like a simple AI integrated frontend project rather than a difficult one.

---

## Who Is This For

Beginners who are really interested in the frontend connectivity with the AI service but get scared on seeing those errors and not knowing how to solve them.

---

## Installation

```bash
pip install gemconnect
```

You also need the Gemini package:

```bash
pip install google-genai
```

---

## How To Use

```python
from google import genai
from gemconnect import ask_gemini

# you bring your own client
client = genai.Client(api_key="YOUR_API_KEY")

# one line to call Gemini safely
result = ask_gemini("What is Python?", client, "gemini-2.5-flash")
print(result)
```

---

## How It Works Inside

```
User writes ask_gemini()
↓
connector.py runs
↓
        try:
        calls Gemini API with
        prompt, client, model
        ↓
        ┌─────────────────┐
        │                 │
     SUCCESS            ERROR
        │                 │
        ↓                 ↓
  response.text      scary error
        │                 │
        ↓                 ↓
returned to user    errors.py translates it
                          │
                          ↓
                    simple message
                    returned to user
```

---

## Real Project Example — PDF Summarizer

```python
# BEFORE GemConnect — scary errors possible
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
summary = response.text


# AFTER GemConnect — one line, errors handled
from gemconnect import ask_gemini

summary = ask_gemini(prompt, client, "gemini-2.5-flash")
```

---

## What Errors GemConnect Covers

These are real errors collected from real beginner projects:

### Setup Errors
```
❌ jinja2.exceptions.TemplateNotFound
✅ Flask cannot find your HTML file. Make sure your folder is named exactly templates.

❌ ERR_CONNECTION_REFUSED
✅ Flask is not running. Check for the app.run() properly.

❌ FutureWarning: google.generativeai has ended
✅ Your Gemini package is outdated. Try to update to new package.
```

### API Key Errors
```
❌ 401 Unauthorized
✅ Unauthorized - check whether the credentials is valid, check whether
   the url is misconfiguration or invalid/expired tokens.
```

### Quota Errors
```
❌ 429 RESOURCE_EXHAUSTED
✅ Your project quota is exhausted. Create a brand new project
   at aistudio.google.com/apikey.

❌ 429 Too Many Requests
✅ Too many requests sent, so wait for a short duration before retrying
   as the model has no free tier now.
```

### Model Errors
```
❌ 404 models/gemini-1.5-flash is not found
✅ Model not found. Run gemconnect.list_models() to see whats available.
```

### Gemini Server Errors
```
❌ 503 UNAVAILABLE
✅ Too many people using it at the same time, so wait a few minutes and try again.

❌ 500 Internal Server Error
✅ Gemini had an unexpected crash internal error.
```

### Frontend Errors
```
❌ blocked by CORS policy
✅ Even though the frontend and backend both are localhost, but they have
   different ports so better use CORS(app) to overcome this problem.

❌ SyntaxError: Unexpected token
✅ The Flask server crashed and sent an Internal Server Error webpage
   instead of JSON. Check the terminal for python crash.
```

---

## Check Available Models

Not sure which model to use? Run this:

```python
from google import genai
from gemconnect import list_models

client = genai.Client(api_key="YOUR_API_KEY")
list_models(client)
```

This prints all models your API key can access.

---

## What GemConnect Supports — v1.0

```
Works with:
✅ PDF Summarizer    (extract text first, pass as string)
✅ Chatbot           (conversation as plain string)
✅ Text Summarizer   (plain text input)
✅ CSV Analyzer      (convert to string with df.to_string())
✅ Any project where input to Gemini is plain text

Coming in v2.0:
🔜 Image support
🔜 Audio support
🔜 Video support
```

## Check Version

```python
import gemconnect
print(gemconnect.__version__)
```

---

## Built From Real Mistakes

This library was not built from assumptions. Every error message inside GemConnect was collected from real beginner projects — PDF summarizer, chatbot, image describer, audio transcriber. Each scary error was faced, documented, and translated into a simple message.

---

*GemConnect v1.0 — Built from real beginner mistakes, for real beginners.*
