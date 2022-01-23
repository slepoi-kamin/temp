
def duplicate_encode(word):
    encoded = ''
    for digit in (word.count(char) for char in word.lower()):
        if digit > 1:
            encoded += ')'
        else:
            encoded += '('
    return encoded


if __name__ == '__main__':
    print(duplicate_encode("oD)ruVdp"))
