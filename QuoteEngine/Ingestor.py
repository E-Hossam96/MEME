"""The main ingestor interface the handles any file type via a strategy."""


from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """Parse all file types."""

    ingestors = [CSVIngestor, TextIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file and returns a list of Quote objects."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
