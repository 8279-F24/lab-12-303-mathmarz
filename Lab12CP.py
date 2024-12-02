import time
import board
import neopixel

dot_length = input('Enter length of dots between 0 and 1')
dash_length = (dot_length * 3)
symbol_gap = dot_length
character_gap = (dot_length * 3)
_color = (125, 125, 125)
brightness = 0.5


def light(self, on=True):
    if on:
        pixels.fill(self._color)
    else:
        pixels.fill((0, 0, 0))
    pixels.show()

def showDot(self):
    self.light(True)
    time.sleep(dot_length)
    self.light(False)
    time.sleep(symbol_gap)

def showDash(self):
    self.light(True)
    time.sleep(dash_length)
    self.light(False)
    time.sleep(symbol_gap)

def display(self, code=".-.-.- "):
        # iterate through morse code symbols
        for c in code:
            # show a dot
            if c == ".":
                self.showDot()
            # show a dash
            elif c == "-":
                self.showDash()
            # show a gap
            elif c == " ":
                time.sleep(character_gap)

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

user_input = input("What is the message?")

message_upper_case = user_input.upper()



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



display(s)