from app.models import HealthEntry
from db import (create_entry, get_entries, update_entry, delete_entry, search_notes, search_food_tolerance,
                get_entries_by_energy, get_entries_by_pain)

def main():
    try:
        entry = HealthEntry(
            energy_level=4,
            pain_level=4,
            sensory_load=7,
            food_tolerance="toast tolerated",
            note="noise sensitivity high"
        )
        create_entry(entry)

        update_entry(3, 9)
        entries = get_entries()

        for entry in entries:
            print(entry)
        print("\n")

        if not entries:
            print("No entries")
            return
        latest_entry_id = entries[0].id
        print(latest_entry_id)
        delete_entry(latest_entry_id)
        delete_entry(11)
        entries = get_entries()

        for entry in entries:
            print(entry)

        # search
        print("\n")
        note_results = search_notes("noise")
        print("results with keyword \"noise\"")
        print_results(note_results)

        print("")
        food_results = search_food_tolerance("toast")
        print("results with food-keyword \"toast\"")
        for f_result in food_results:
            print(f_result)

        print("")
        energy_results = get_entries_by_energy(9)
        print("results with energy = 9")
        print_results(energy_results)

        print("")
        pain_results = get_entries_by_pain(9)
        print("results with pain = 9")
        print_results(pain_results)
    except ValueError as e:
        print(e)

def print_results(results):
    if len(results) == 0:
        print("No results")
        return
    for result in results:
        print(result)


if __name__ == "__main__":
    main()

