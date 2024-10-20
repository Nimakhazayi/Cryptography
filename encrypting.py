
txt = str(input(" File address please: "))
const = int(input(" The constant of a linear replacement you want in order of the English alphabet: "))
coef = int(input(" The coeff of a linear replacement you want in order of the English alphabet:\n choose from the list of [1,3,5,7,9,11,15,17,19,21,23,25]:  "))
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipher = []

def encrypting(b):
    file = open(f"{b}", "r")
    content = file.read()
    for i in content:
        if i == " ":
            cipher.append(" ")
        elif i == "\n":
            cipher.append("\n")
        elif i == ".":
            cipher.append(".")
        elif i == "?":
            cipher.append("?")
        elif i == "!":
            cipher.append("!")
        elif i == ",":
            cipher.append(",")
        else:
            j = alphabet.index(i)
            index = ((j + 1)*coef + const) % 26
            cipher.append(alphabet[index - 1])
    encrypted = "".join(cipher)
    print(f"\n{encrypted}")
    file.close()

encrypting(txt)
