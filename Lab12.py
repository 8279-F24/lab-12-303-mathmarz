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
    '0':'-----', 'SPACE' : ' ', 'END-WORD' : '.......'}

# a. prompts the user for a sentence.
user_input = input("What is the message?")

# b. convert the sentence to lowecase and remove any character/number without a morse code equivalent
message_upper_case = user_input.upper()

#[MY,NAME,IS]

message = message_upper_case.replace("!@#$%^&*()_+-=~`[]{}|;:'\",<.>/?", "").split()

final = []

#[MY,NAME,IS]

for i in message:
    for char in i:
        letter = morse_code_dict[char]
        final.append(letter)
        final.append(morse_code_dict['SPACE'])
    final.append(morse_code_dict['END-WORD'])
    final.append(morse_code_dict['SPACE'])

del final[-3:]
#final[:-3]

s = ''.join(map(str,final))

print(s)

