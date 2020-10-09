from search.store import Store
from search.fixtures import records
from pprint import pprint
import os

if __name__ == "__main__":
    store = Store()

    for record in records:
        store.add(record)

    query = os.getenv("SEARCHTERM")

    matches = store.search(query)

    print("## OUTPUT")
    pprint(matches.to_dict)


    print("## JSON")
    pprint(matches.to_json)
