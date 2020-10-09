from .record import Record, RecordResult
from .texttools import normalize

class Store:
    def __init__(self):
        self.index = RecordResult()

    def add(self, text):
        """Adds a record"""
        record = Record(text)
        self.index.add(record)

    def search(self, term):
        """Searches index for matching term and returns RecordResult of matches"""
        term_sanitized = normalize(term)
        matches = RecordResult()
        for record in self.index.records:
            if term_sanitized in record.terms:
                matches.add(record)
        return matches
