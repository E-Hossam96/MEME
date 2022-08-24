"""Interface ingestor abstract base class."""


from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class `Ingestorinterface`."""

    allowed_exensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check for validity and returns True or False."""
        return path.split('.')[-1] in cls.allowed_exensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse function to be override by the subclasses."""
        pass
