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


    print("")
    print("## JSON")
    pprint(matches.to_json)


    print("")
    print("## RESULTS BASED ON WORD FREQUENCY")

    matched_rank_records = store.search_by_rank(query)
    for item in matched_rank_records:
        print(f"ID: {item[0].id}, Text: {item[0].text}, Score: {item[1]}")
