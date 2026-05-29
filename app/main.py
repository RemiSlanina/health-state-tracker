from db import (create_entry, get_entries, update_entry, delete_entry, search_notes, search_food_tolerance,
                get_entries_by_energy, get_entries_by_pain)

def main():
    try:
        create_entry(
            4,5,7,"toast tolerated", "noise sensitivity high"
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

