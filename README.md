# URL shorterner - exam 4 - CS 54



## Context

This was a ***4 hour*** exam as part of my studies in Telecom Nancy. The goal was to create short keys that can be used to access specific web pages, then the user would only have to memorize the key to access the longer and more troublesome to remember site.

For example, 'https://github.com/Zarakinn/url-shortener-exam-CS54' can be shorten to 'http://localhost:5454:/xyz'.

The task was to create and store the code correctly and redirect to the long website when they are entered. An added bonus was to remember how many time the redirection was used.

## Tech Stack

Python3, Flask, SQLite, html, CSS.

### How to use ?

The main part of the code is in 'app.py'

To launch the website, in the same folder as 'app.py' use :

```bash
# Create a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Dependencies installation
$ pip install -r requirements.txt

# Execution
$ flask run --host=0.0.0.0 --port=5454
```

Use the display button to see all the shorten url, how many time they have been used and where they lead to.

On the add page, you can choose the short url to link to the long website and add it.

On the shorten page, an url is generated for you.

There is basic error handling and link deletion implemented.

The website is pretty ugly, but as it was a 4 hour project and I was pretty new to programming, look was not my priority.

## Credit

The exam was created by Telecom Nancy and the original Readme.md is the ![enonce.pdf](https://github.com/Zarakinn/url-shortener-exam4-CS54/blob/master/README.md) ( in French).
