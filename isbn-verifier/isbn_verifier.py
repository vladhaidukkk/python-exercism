def is_valid(isbn):
    scrubbed_isbn = isbn.replace("-", "")
    nums = []

    for index, char in enumerate(scrubbed_isbn):
        if char in "0123456789":
            nums.append(int(char))
        elif char == "X" and index == len(scrubbed_isbn) - 1:
            nums.append(10)
        else:
            return False
    
    return sum([num * (len(nums) - index) for index, num in enumerate(nums)]) % 11 == 0 if len(nums) == 10 else False
