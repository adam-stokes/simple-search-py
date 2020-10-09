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
    count_map = []
    for record in matches.records:
        count_map.append((int(record.term_frequency[query]["count"]), record))
    count_map.sort(key=lambda x:x[0], reverse=True)
    for count, record in count_map:
        print(f"ID: {record.id}, Text: {record.text}, Score: {record.term_frequency[query]['count']}")
