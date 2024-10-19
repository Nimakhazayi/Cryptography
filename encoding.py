
txt = str(input(" File address please: "))
const = int(input(" The constant of a linear replacement you want in order of the English alphabet: "))
coef = int(input(" The coeff of a linear replacement you want in order of the English alphabet: "))
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipher = []

def encoding(b):
    file = open(f"{b}", "r")
    content = file.read()
    content = content.replace(" ", "")
    content = content[:-1]
    for i in content:
        j = alphabet.index(i)
        index = ((j + 1)*coef + const) % 26
        cipher.append(alphabet[index - 1])
    print(f"\n{cipher}")
    file.close()

encoding(txt)