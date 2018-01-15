# Braille Translation 2

sent = "the quick brown fox jumped over the lazy dog"
temp = "011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
val = {'s' : '011100'}
for i in sent:
    val[i] = temp[0:6]
    temp = temp[6:]

def answer(plaintext):
    if(len(plaintext) > 50 ):return -1
    out = ""
    for i in plaintext:
        if(i.isupper()):out = out + "000001";i = i.lower()
        out = out + val[i]
    return out

print answer("code")