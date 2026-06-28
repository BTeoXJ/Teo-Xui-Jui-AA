def merge_sort(transactions):
    """Sorts transactions by transaction_id using recursive Merge Sort. Returns a new sorted list."""

    # Base case: a list with zero or one item is already sorted.
    if len(transactions) <= 1:
        return transactions

    # Divide step: split the list into two halves.
    middle = len(transactions) // 2
    left_half = transactions[:middle]
    right_half = transactions[middle:]

    # Conquer step: sort both halves recursively.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Combine step: merge the two sorted halves.
    return merge(sorted_left, sorted_right)

def merge(left_half, right_half):
    """Combines two sorted transaction lists into one sorted list."""

    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index].transaction_id <= right_half[right_index].transaction_id:
            merged_list.append(left_half[left_index])
            left_index += 1
        else:
            merged_list.append(right_half[right_index])
            right_index += 1

    # Add any remaining transactions from the left side.
    merged_list.extend(left_half[left_index:])

    # Add any remaining transactions from the right side.
    merged_list.extend(right_half[right_index:])

    return merged_list

def binary_search(transactions, target_id):
    """Searches for a transaction ID using Binary Search. The transaction list must already be sorted."""

    low = 0
    high = len(transactions) - 1

    while low <= high:
        middle = (low + high) // 2
        current_id = transactions[middle].transaction_id

        if current_id == target_id:
            return transactions[middle]

        if current_id < target_id:
            low = middle + 1
        else:
            high = middle - 1

    return None

def linear_search(transactions, target_id):
    """Searches for a transaction by checking one item at a time."""

    for transaction in transactions:
        if transaction.transaction_id == target_id:
            return transaction

    return None




