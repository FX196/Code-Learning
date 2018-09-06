MORSE_CODE = {}


def decodeMorse(morse_code):
    # Accept dots, dashes and spaces, return human-readable message
    while morse_code[0] == " ":
        morse_code = morse_code[1:]
    while morse_code[-1] == " ":
        morse_code = morse_code[:-1]
    morse_code = morse_code.replace("   ", "  ")
    return "".join([MORSE_CODE[x] if x else " " for x in morse_code.split(" ")])
