import pytest

from search.texttools import normalize
from search.record import Record
from search.store import Store
from search.fixtures import records

def test_string_normalized():
    """Test if string is normalized"""

    string = "The broken window shatters across the ground!"
    expected = "the broken window shatters across the ground"

    assert normalize(string) == expected


def test_string_frequency():
    """Test frequency counting"""
    string = "There is that one person and only that one person"
    record = Record(string)

    assert record.term_frequency["person"] == 2
    assert record.term_frequency["there"] == 1


def test_string_result_found():
    """Test that a matching result is found"""
    store = Store()
    for record in records:
        store.add(record)

    assert store.search("GrEaTeST").count == 1
    assert store.search("life").count == 4
    assert store.search("life!").count == 4
    assert store.search(",life,").count == 4
