"""Flask applicaion to render meme photos.

The file conatins four functions:
    - One function to handle the setup execution.
    - Three decorated functions for rendering the templates.
"""


import random
import os
from urllib import response
import requests
import subprocess
from flask import Flask, render_template, abort, request

# Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes += Ingestor.parse(file)

    quotes = [q for q in quotes if q is not None]

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    assert quote is not None
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form['image_url']
    response = requests.get(image_url)

    local_img = f'temp{random.randint(0, 1000)}.png'
    with open(local_img, 'wb') as fid:
        fid.write(response.content)

    quote_body = request.form['body']
    quote_author = request.form['author']
    quote = QuoteModel(quote_body, quote_author)

    path = meme.make_meme(local_img, quote.body, quote.author)

    subprocess.run(['del', local_img], shell=True)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
