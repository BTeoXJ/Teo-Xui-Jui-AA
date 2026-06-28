import time

from transaction import Transaction
from algorithms import merge_sort, binary_search, linear_search


def load_sample_data():
    """Returns an unsorted list of online shopping transactions."""

    return [
        Transaction("TRX108", "Teo Xui Jui", "Wireless Mouse", 49.90, "07-06-2026"),
        Transaction("TRX102", "Cheong Yi Quan", "USB-C Cable", 18.50, "03-06-2026"),
        Transaction("TRX115", "Ming Zhe", "Mechanical Keyboard", 189.00, "20-06-2026"),
        Transaction("TRX104", "Jun Sheng", "Phone Case", 25.90, "12-06-2026"),
        Transaction("TRX111", "Daniel Lim", "Laptop Stand", 79.90, "16-06-2026"),
        Transaction("TRX101", "Mellisa", "Bluetooth Earbuds", 129.00, "01-06-2026"),
        Transaction("TRX109", "Jason", "Webcam", 95.50, "13-06-2026"),
        Transaction("TRX106", "Yu Ze", "Power Bank", 69.90, "10-06-2026"),
        Transaction("TRX113", "Jia Jun", "Monitor Light Bar", 59.00, "18-06-2026"),
        Transaction("TRX103", "Yun Pei", "Notebook Sleeve", 42.00, "05-06-2026"),
        Transaction("TRX110", "Jun Jie", "HDMI Adapter", 35.90, "14-06-2026"),
        Transaction("TRX105", "Aidan", "Portable SSD", 249.00, "08-06-2026")
    ]


def display_transactions(transactions, title):
    """Displays a list of transactions in a readable format."""

    print(f"\n========== {title} ==========")
    print("Transaction | Customer Name      | Product Name          | Amount       | Date")
    print("-" * 86)

    for transaction in transactions:
        print(transaction)


def display_menu():
    """Displays the main menu."""

    print("\n==============================================")
    print("   CUSTOMER TRANSACTION SORTING AND SEARCH")
    print("==============================================")
    print("1. Display original transactions")
    print("2. Sort transactions using Merge Sort")
    print("3. Search transaction using Binary Search")
    print("4. Search transaction using Linear Search")
    print("5. Compare execution time")
    print("6. Exit")


def sort_transactions(transactions):
    """Sorts transactions and displays before and after results."""

    display_transactions(transactions, "TRANSACTIONS BEFORE SORTING")

    start_time = time.perf_counter_ns()
    sorted_transactions = merge_sort(transactions)
    elapsed_time = time.perf_counter_ns() - start_time

    display_transactions(sorted_transactions, "TRANSACTIONS AFTER MERGE SORT")
    print(f"\nMerge Sort Time: {elapsed_time:,} ns")

    return sorted_transactions


def search_using_binary_search(sorted_transactions):
    """Searches for a transaction using Binary Search."""

    if sorted_transactions is None:
        print("\nPlease choose option 2 first to sort the transactions.")
        return

    target_id = input("\nEnter transaction ID to search: ").upper()

    start_time = time.perf_counter_ns()
    result = binary_search(sorted_transactions, target_id)
    elapsed_time = time.perf_counter_ns() - start_time

    if result is None:
        print("Transaction not found.")
    else:
        print("\nTransaction found:")
        print(result)

    print(f"Binary Search Time: {elapsed_time:,} ns")


def search_using_linear_search(transactions):
    """Searches for a transaction using Linear Search."""

    target_id = input("\nEnter transaction ID to search: ").upper()

    start_time = time.perf_counter_ns()
    result = linear_search(transactions, target_id)
    elapsed_time = time.perf_counter_ns() - start_time

    if result is None:
        print("Transaction not found.")
    else:
        print("\nTransaction found:")
        print(result)

    print(f"Linear Search Time: {elapsed_time:,} ns")


def compare_execution_time(transactions, sorted_transactions):
    """Measures Merge Sort, Binary Search, and Linear Search execution time."""

    if sorted_transactions is None:
        sorted_transactions = merge_sort(transactions)

    target_id = "TRX110"
    repetitions = 5000

    print("\n========== EXECUTION TIME COMPARISON ==========")
    print(f"Test transaction ID: {target_id}")
    print(f"Each search is repeated {repetitions:,} times.\n")

    start_time = time.perf_counter_ns()
    merge_sort(transactions)
    merge_sort_time = time.perf_counter_ns() - start_time

    start_time = time.perf_counter_ns()

    for _ in range(repetitions):
        binary_search(sorted_transactions, target_id)

    binary_search_time = time.perf_counter_ns() - start_time

    start_time = time.perf_counter_ns()

    for _ in range(repetitions):
        linear_search(transactions, target_id)

    linear_search_time = time.perf_counter_ns() - start_time

    print(f"Merge Sort Time (one sort)        : {merge_sort_time:,} ns")
    print(f"Binary Search Time ({repetitions:,} searches): {binary_search_time:,} ns")
    print(f"Linear Search Time ({repetitions:,} searches): {linear_search_time:,} ns")

    if binary_search_time < linear_search_time:
        print("\nResult: Binary Search was faster than Linear Search.")
    else:
        print("\nResult: Linear Search was faster in this test.")

def main():
    """Runs the Customer Transaction Sorting and Searching System."""

    transactions = load_sample_data()
    sorted_transactions = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_transactions(transactions, "ORIGINAL UNSORTED TRANSACTIONS")

        elif choice == "2":
            sorted_transactions = sort_transactions(transactions)

        elif choice == "3":
            search_using_binary_search(sorted_transactions)

        elif choice == "4":
            search_using_linear_search(transactions)

        elif choice == "5":
            compare_execution_time(transactions, sorted_transactions)

        elif choice == "6":
            print("Thank you for using the Transaction System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()


