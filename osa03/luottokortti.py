'''
Testikorttien numerot saatu osoitteesta
https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm
'''
visa = '4111111111111111'
mastercard = '5105105105105100'
amex = '378282246310005'


kortti = visa

if kortti[0] == '4':
    print('Visa')
elif 51 <= int(kortti[:2]) <= 55 or 2221 <= int(kortti[:4]) <= 2720:
    print('Mastercard')
else:
    print('Tuntematon kortti')
