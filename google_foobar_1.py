def make_code():
    plaintext = "the quick brown fox jumps over the lazy dog"
    output = "011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    code = {}
    i = 0
    for c in plaintext:
        encoded = output[i : i + 6]
        if c in code:
            assert code[c] == encoded
        else:
            code[c] = encoded
        i += 6
    return code


CAPITALIZE = "000001"

CODE = make_code()


def solution(plaintext):
    encoded = ""
    for c in plaintext:
        if c.isupper():
            encoded += CAPITALIZE
        encoded += CODE[c.lower()]
    return encoded


if False:
    input = "The quick brown fox jumps over the lazy dog"
    output = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    assert solution(input) == output