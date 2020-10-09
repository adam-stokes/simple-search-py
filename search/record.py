import uuid
import string
import json
from .texttools import normalize

class Record:
    def __init__(self, text):
        self.id = uuid.uuid4()

        self.original_text = text
        self.text = normalize(text)

    @property
    def terms(self):
        """Returns list of keywords
        """
        return [term for term in self.text.split(" ")]

    @property
    def term_frequency(self):
        """Returns dictionary containing the term and their frequency in text. """
        return {term: self.text.count(term) for term in self.terms}

    def __dict__(self):
        """Return dictionary representation of record"""
        return {str(self.id): {"terms": self.terms, "original_text": self.original_text, "text": self.text, "frequency": self.term_frequency}}


class RecordResult:
    def __init__(self):
        self.records = []

    @property
    def count(self):
        """Return number of results found"""
        return len(self.records)

    def add(self, record):
        """Add a record to results"""
        self.records.append(record)

    @property
    def to_json(self):
        """Return json output of results"""
        return json.dumps([record.__dict__() for record in self.records])
