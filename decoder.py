from morsewords import MORSE_CODE_DICT as mcd


def encrypt_string(string):
    sentence = string.upper()
    result = ""

    for i in range(0, len(sentence)):
        result += mcd[sentence[i]] + " "

    return result


print(encrypt_string(
    "Infinite striving to be the best is man's duty; it is its own reward. Everything else is in God's hands."))