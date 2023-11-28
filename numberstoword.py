def number_to_word(number):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    if number == 0:
        return ones[0]
    elif number < 0:
        return 'minus ' + number_to_word(abs(number))
    elif number < 10:
        return ones[number]
    elif number < 20:
        return teens[number - 11]
    elif number < 100:
        return tens[number // 10 - 1] + (' ' + ones[number % 10] if number % 10 != 0 else '')
    elif number < 1000:
        return ones[number // 100] + ' hundred' + (' ' + number_to_word(number % 100) if number % 100 != 0 else '')
    elif number < 1000000:
        return number_to_word(number // 1000) + ' thousand' + (' ' + number_to_word(number % 1000) if number % 1000 != 0 else '')
    elif number < 1000000000:
        return number_to_word(number // 1000000) + ' million' + (' ' + number_to_word(number % 1000000) if number % 1000000 != 0 else '')
    else:
        return 'number out of range'

print(number_to_word(200))