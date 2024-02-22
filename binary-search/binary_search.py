def find(search_list, value):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        item = search_list[mid]

        if item == value:
            return mid
        elif item < value:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("value not in array")
