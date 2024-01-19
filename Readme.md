# Python and Flask Setup Guide

## Installation

1. Install Python version 3.12 or greater from [https://www.python.org/downloads/](https://www.python.org/downloads/).

## Pip Commands

Use the following pip command to install Flask:

```bash
pip install Flask
```

## Steps to Set Up Flask Server

1. Execute the commands above.
2. Create an `app.py` file and import the following modules using:
```python
from flask import Flask, redirect, render_template
```
3. Activate the flask app with
```python
app = (__name__)
```
4. Create your first route with
```python
@app.route("/")
def home():
    print("Hello world")
```
5. Create a templates folder (MUST BE NAMED TEMPLATES) and create an index.html file with your desired html.
6. Within the home function write 
```python
return render_template("index.html")
```
7. If you wish to pass data or variables to the html add a second arg
```python 
return render_template("index.html", name="Landon")
```
the name varible is the accesable in the html file using jinja syntax 
```html
<h1>Hello {{ name }}</h1>
```

To run your Flask app run the command 
```bash
flask run
```

# Happy Coding!
Ps. PLEASE ask questions if you get stuck anywhere I am always happy to help! Just @ me in discord or DM me.