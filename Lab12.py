morse_code_dict = {'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

# a. prompts the user for a sentence.
user_input = input("What is the message?")

# b. convert the sentence to lowecase and remove any character/number without a morse code equivalent
message_upper_case = user_input.upper()

message = message_lower_case.replace("!@#$%^&*()_+-=~`[]{}|;:'\",<.>/?", "")

print(message)

# ???????? PRECISO MUDAR AS LETRAS DO CODIGO PARA MINUSCULO???? ????????

