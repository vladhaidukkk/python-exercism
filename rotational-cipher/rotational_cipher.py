MIN_UPPER_CODE = ord("A")
MAX_UPPER_CODE = ord("Z")
MIN_LOWER_CODE = ord("a")
MAX_LOWER_CODE = ord("z")

def rotate(text, key):
    def rotate_char(char):
        if not char.isalpha():
            return char
        min_code, max_code = (MIN_UPPER_CODE, MAX_UPPER_CODE) if char.isupper() else (MIN_LOWER_CODE, MAX_LOWER_CODE)
        new_code = ord(char) + key
        return chr(min_code + new_code - max_code - 1 if new_code > max_code else new_code)
    
    return "".join([rotate_char(char) for char in text])
