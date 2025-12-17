tekst = input("Geef de tekst die je wilt encrypten: ")

versleuteld = ""

for letter in tekst:
    # kleine letters
    if 'a' <= letter <= 'z':
        nieuwe_code = ord(letter) + 5
        if nieuwe_code > ord('z'):
            nieuwe_code -= 26
        versleuteld += chr(nieuwe_code)

    # hoofdletters (extra netjes)
    elif 'A' <= letter <= 'Z':
        nieuwe_code = ord(letter) + 5
        if nieuwe_code > ord('Z'):
            nieuwe_code -= 26
        versleuteld += chr(nieuwe_code)

    # andere tekens blijven gelijk
    else:
        versleuteld += letter

print(versleuteld)
