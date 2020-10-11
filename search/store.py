from .record import Record, RecordResult
from .texttools import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

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

    def search_by_rank(self, term):
        """This search results pairing them with a ranked similarity of the search term

        Note: this does not account for things such as stopwords
        """
        matched_records = self.search(term)

        doc_vectors = TfidfVectorizer().fit_transform([term] + [record.text for record in matched_records.records])
        cosine_similarites = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
        document_scores = [item.item() for item in cosine_similarites[1:]]

        # Merge the records with their scores since the lists are ordered
        merged_matched_records = list(zip([record for record in matched_records.records], document_scores))

        # Sort by highest rank
        merged_matched_records.sort(key=lambda x:x[1], reverse=True)
        return merged_matched_records
