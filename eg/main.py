from search.store import Store
from search.fixtures import records
import os

if __name__ == "__main__":
    store = Store()

    for record in records:
        store.add(record)

    query = os.getenv("SEARCHTERM")

    matches = store.search(query)

    print(matches.to_json)
