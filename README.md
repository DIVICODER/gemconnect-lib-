# GemConnect

**GemConnect sits between Flask and Gemini, calls the API safely, and if anything goes wrong, translates the scary technical error into a simple message the beginner can understand and fix.**

---

## The Problem

As an engineer, it felt fascinating to connect upcoming trends like AI into a website and see it work. Getting Gemini to respond in the terminal felt exciting. But when I tried to connect it with the frontend, it once again felt like zero.

Errors kept coming when interconnecting the frontend with Flask. Initially I tried to debug on my own, but it reached a threshold where I shifted from being curious and excited to a mood of just finishing what I had started. I kept copy-pasting the error to an AI bot to debug. Sometimes it worked, sometimes it didn't. But whether it worked or not, I hadn't been able to debug the error myself.

The errors were in technical terms like "404" — like these types of numbers. And in some cases it would show a scary list of errors and say "JSON error" like that, making it difficult to understand what went wrong and where.

What I needed was an error document to understand each error. That problem led to the creation of this library.

---

## What GemConnect Does

GemConnect gets the scary error and converts it into a human-understandable message for easy debugging.

```
WITHOUT GemConnect:
Flask → Gemini → 😵 Scary JSON error dump → Beginner gives up

WITH GemConnect:
Flask → GemConnect → Gemini → ❌ Error?
                                    ↓
                        "Hey! Your API key looks wrong.
                         Go to aistudio.google.com/apikey and get a fresh one."
```

---

## Who Is This For

Beginners who are really interested in frontend connectivity with AI services but get scared seeing those errors and not knowing how to solve them.

---

## Requirements

Before using GemConnect, install the Gemini package:

```
pip install google-genai
```

GemConnect itself has zero dependencies. You are responsible for creating and passing the Gemini client.

---

## Installation

```
pip install gemconnect
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

## Input Validation

GemConnect checks your inputs before even calling Gemini. If something is wrong it tells you immediately in plain English:

```python
ask_gemini(None, client, model)
# → "Your prompt is None. Please pass a text string like ask_gemini('hello', client, model)."

ask_gemini("", client, model)
# → "Your prompt is empty. Please type something before sending."

ask_gemini(["hello"], client, model)
# → "Your prompt must be plain text. You passed a list instead of a string."

ask_gemini(prompt, None, model)
# → "Your Gemini client is None. Make sure you created it using genai.Client(api_key=...)."

ask_gemini(prompt, client, None)
# → "You forgot to pass a model name. Try ask_gemini(prompt, client, 'gemini-2.0-flash')."

ask_gemini(prompt, client, "")
# → "Your model name is empty. Try ask_gemini(prompt, client, 'gemini-2.0-flash')."
```

---

## How It Works Inside

```
User writes ask_gemini()
        ↓
connector.py runs input checks
        ↓
        ┌─────────────────────────┐
        │                         │
  checks pass               checks fail
        │                         │
        ↓                         ↓
  calls Gemini API        friendly message
        │                  returned to user
        ↓
  ┌─────────────┐
  │             │
SUCCESS       ERROR
  │             │
  ↓             ↓
response.text  errors.py
  │             │
  ↓             ↓ Layer 1 — keyword match
returned      errors.py
to user        │
               ↓ Layer 2 — synonym match
               │
               ↓
         simple message
         returned to user
```

---

## Real Project Example — Chatbot

```python
# BEFORE GemConnect — scary errors possible
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=conversation
)
ai_reply = response.text


# AFTER GemConnect — one line, errors handled
from gemconnect import ask_gemini

ai_reply = ask_gemini(conversation, client, "gemini-2.5-flash")
```

---

## What Errors GemConnect Covers

Every error message inside GemConnect was collected from real beginner projects. Two layers of matching make sure as many errors as possible are caught.

### Setup Errors
```
❌ jinja2.exceptions.TemplateNotFound
✅ Flask cannot find your HTML file. Make sure your HTML file is inside 
   a folder named exactly 'templates' (no capital letters, no spaces).

❌ ERR_CONNECTION_REFUSED
✅ Your Flask server is not running. Go to your terminal and run your 
   app.py file first, then try again.

❌ FutureWarning: google.generativeai has ended
✅ Your Gemini package is old. Open your terminal and run: 
   pip install --upgrade google-generativeai
```

### Install Errors
```
❌ ModuleNotFoundError: No module named 'google.generativeai'
✅ A required package is not installed. Open your terminal and run: 
   pip install google-generativeai
```

### API Key Errors
```
❌ 401 Unauthorized
✅ Gemini does not recognize you. Your API key is either wrong, expired, 
   or missing. Go to aistudio.google.com/apikey and get a fresh one.

❌ API key not valid. Please pass a valid API key.
✅ Your API key is wrong. Go to aistudio.google.com/apikey, copy your 
   key again and paste it carefully — even one wrong character breaks it.
```

### Quota Errors
```
❌ RESOURCE_EXHAUSTED
✅ You have used up all your free Gemini quota. Go to 
   aistudio.google.com/apikey, create a brand new project and generate 
   a new API key from there.

❌ 429 Too Many Requests
✅ You sent too many requests too fast. Wait 30-60 seconds and try again.
```

### Model Errors
```
❌ 404 models/gemini-1.5-flash is not found
✅ The model name you typed does not exist. Run list_models() to see the 
   exact names and copy-paste one of those.
```

### Gemini Server Errors
```
❌ InternalServerError
✅ Something crashed on Gemini's side — this is not your fault. 
   Wait a minute and try the exact same request again.

❌ 503 UNAVAILABLE
✅ Too many people are using Gemini right now. Wait a few minutes and try again.

❌ 504 Timeout
✅ Gemini took too long to reply. Wait a moment and try again.
```

### Network Errors
```
❌ ConnectionError
✅ Could not reach Gemini. Check your internet connection and try again.

❌ SSLError
✅ A secure connection to Gemini failed. Check your internet or try a 
   different network.
```

### Frontend Errors
```
❌ blocked by CORS policy
✅ Your browser is blocking the request because your frontend and backend 
   are on different ports. Install flask-cors and add CORS(app) to your Flask file.

❌ SyntaxError: Unexpected token
✅ Your Flask server crashed and sent back an error page instead of data. 
   Check your terminal — the real error is printed there.
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
✅ PDF Summarizer      (extract text first, pass as string)
✅ Chatbot             (conversation as plain string)
✅ Text Summarizer     (plain text input)
✅ CSV Analyzer        (convert to string with df.to_string())
✅ Any project where input to Gemini is plain text

Coming in v2.0:
🔜 Image support
🔜 Audio support
🔜 Video support
```

---

## Check Version

```python
import gemconnect
print(gemconnect.__version__)
```

---

## Built From Real Mistakes

This library was not built from assumptions. Every error message inside GemConnect was collected from real beginner projects — PDF summarizer, chatbot, image describer, audio transcriber. Each scary error was faced, documented, and translated into a simple message.

**GemConnect v1.0 — Built from real beginner mistakes, for real beginners.**
