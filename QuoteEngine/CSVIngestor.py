"""Ingestor to parse csv files."""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    """The main class to handle csv files."""

    allowed_exensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Process a file and return a list of Quote objects."""
        qdf = pd.read_csv(path, header=0)
        quotes = [None] * len(qdf)
        for i in range(len(qdf)):
            quotes[i] = QuoteModel(qdf.loc[i].body, qdf.loc[i].author)
        return quotes
