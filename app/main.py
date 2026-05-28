
from db import create_entry, get_entries, update_entry, delete_entry

def main():
    create_entry(
        4,5,7,"rice tolerated", "noise sensitivity high"
    )

    update_entry(3, 9)
    entries = get_entries()

    for entry in entries:
        print(entry)
    print("\n")

    latest_entry_id = entries[0][0]
    print(latest_entry_id)
    delete_entry(latest_entry_id)
    delete_entry(4)
    entries = get_entries()

    for entry in entries:
        print(entry)

if __name__ == "__main__":
    main()

