def is_interesting(number, awesome_phrases):
    if (number > 97):
        if number in awesome_phrases:
            return 2

        if (number == 98) or (number == 99):
            return 1

        if (number + 1 in awesome_phrases) or (number + 2 in awesome_phrases):
            return 1

        if is_interesting_number(number):# на эту милю
            return 2

        if is_interesting_number(number + 1) or is_interesting_number(number + 2): # на две сосед. мили
            return 1
    return 0


def is_interesting_number(num):
    string = str(num)
    set_val = set(string)

    if (len(set_val) == 1): #проверка на все одинаковые символы
        return True
    
    if (string in '1234567890 9876543210'): #проверка на ин(де)кремент
        return True
    
    if (string == string[::-1]): #проверка на палиндром
        return True
    
    if ('0' in set(string[1::])) and (len(set(string[1::])) == 1):
        return True
    
    return False

print(is_interesting(99, []))