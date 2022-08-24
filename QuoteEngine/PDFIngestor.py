"""Ingestor to parse pdf files."""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess


class PDFIngestor(IngestorInterface):
    """The main class to handle pdf files."""

    allowed_exensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Process a file and return a list of Quote objects."""
        quotes = []
        p = subprocess.Popen(
            ['pdftotext', '-nopgbrk', path, '-'], stdout=subprocess.PIPE
        )
        data = p.communicate()[0].decode()
        data = data.split('\r\n')
        for line in data:
            if line != '':
                data = line.split(' - ')
                quotes.append(QuoteModel(data[0], data[1]))
        return quotes
