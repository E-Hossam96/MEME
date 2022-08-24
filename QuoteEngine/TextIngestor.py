"""Ingestor to parse text files."""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    """The main class to handle text files."""

    allowed_exensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Process a file and return a list of Quote objects."""
        quotes = []
        with open(path, 'r') as fid:
            for line in fid.readlines():
                if line != '':
                    data = line.split(' - ')
                    quotes.append(QuoteModel(data[0], data[1]))
        return quotes
