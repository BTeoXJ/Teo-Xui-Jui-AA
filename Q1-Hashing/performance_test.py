import time

def linear_search(medicine_list, medicine_id):
    """Searches for a medicine in a normal Python list."""

    for medicine in medicine_list:
        if medicine.medicine_id == medicine_id:
            return medicine

    return None

def performance_comparison(hash_table, medicine_list):
    """Compares Hash Table search time with normal list linear-search time."""

    search_keys = [
        "MED101",  # Existing record
        "MED105",  # Existing record
        "MED110",  # Existing record
        "MED999",  # Non-existing record
        "MED000"   # Non-existing record
    ]

    repetitions = 5000

    print("\n========== PERFORMANCE COMPARISON ==========")
    print(f"Each key is searched {repetitions:,} times.")
    print("Time unit: nanoseconds (ns)\n")

    for medicine_id in search_keys:
        # Measure Hash Table search time
        start_time = time.perf_counter_ns()

        for _ in range(repetitions):
            hash_table.search(medicine_id)

        hash_table_time = time.perf_counter_ns() - start_time

        # Measure normal list linear-search time
        start_time = time.perf_counter_ns()

        for _ in range(repetitions):
            linear_search(medicine_list, medicine_id)

        linear_search_time = time.perf_counter_ns() - start_time

        exists = "Yes" if hash_table.search(medicine_id) is not None else "No"

        print(f"Search Key: {medicine_id}")
        print(f"Record Exists: {exists}")
        print(f"Hash Table Search Time : {hash_table_time:,} ns")
        print(f"Linear Search Time     : {linear_search_time:,} ns")

        if hash_table_time < linear_search_time:
            print("Result: Hash table was faster.\n")
        elif linear_search_time < hash_table_time:
            print("Result: Linear search was faster in this run.\n")
        else:
            print("Result: Both methods produced the same time.\n")



