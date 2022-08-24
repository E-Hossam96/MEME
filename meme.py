"""Generate memes using the CLI.

The file conains the main function to execute the `generate_meme` function.
The `generate_meme` function accepts inputs from the user and processes them.
"""


import os
import random
import argparse

# Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = os.path.normpath("./_data/photos/dog/")
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes += Ingestor.parse(os.path.normpath(f))

        quotes = [q for q in quotes if q is not None]

        quote = random.choice(quotes)
        assert quote is not None
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine(os.path.normpath('./tmp'))
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description='Quote Specs')
    parser.add_argument(
        '--path', type=str, default=None, help='Image Path.'
    )
    parser.add_argument(
        '--body', type=str, default=None, help='Meme Body.'
    )
    parser.add_argument(
        '--author', type=str, default=None, help='Meme Author.'
    )
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
