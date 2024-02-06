def is_armstrong_number(number):
    result = 0
    
    for digit in (str_num := str(number)):
        result += int(digit) ** len(str_num)

    return result == number
