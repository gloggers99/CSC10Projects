
encoded_string = "^a}>c00tA&hjc9dqBvDmc9)nE76eD&toCq6~D,^qcb@/)#6g(*?x@aL."
encoding_table = "GHIJ1234567890abcdefghi~!@#$%^&*()ABCDEF{}[]<>,./?\"jklmnopqrstuvwxyzKLMNOPQRSTUVWXYZ"

def decode(encoded_text, table) -> str:
    mash = ""
    for c in encoded_text:
        for i in range(0, len(table)):
            if table[i] == c:
                mash += str(bin(i - 8)).replace("0b", '').zfill(6)

    result = ""
    for i in range(0, len(mash), 8):
        result += chr(int(mash[i:i+8], 2))
    return result

print(decode(encoded_string, encoding_table))
