import base64

MESSAGE = '''
DU4QHRYLBAEaFhAKVk4EGhAJFVVFERdTGQUPDRQPFBdOEQoQUQwQHBANDBcNFhwQUQwFDhoaFQFO
EQoQUQANCwcNBRsLXVUXWklECRYACBcfVF1VGB1ESE9IRgcHXV9THQwHT1lIRgAIU1JZAhpESE9I
RgEIV1UXWklEDhoHRlJTERdHHwdCTwg=
'''

KEY = 'vichuhari100'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)