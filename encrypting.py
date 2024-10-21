
txt = str(input(" File address please: "))
const = int(input(" The constant of a linear replacement you want in order of the English alphabet: "))
coef = int(input(" The coeff of a linear replacement you want in order of the English alphabet:\n choose from the list of [1,3,5,7,9,11,15,17,19,21,23,25]: "))
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipher = []
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def encrypting(b):
    file = open(f"{b}", "r")
    content = file.read()
    for i in content:
        if i == " ":
            cipher.append(" ")
        elif i == "\n":
            cipher.append("\n")
        elif i == ";":
            cipher.append(";")
        elif i == "'":
            cipher.append("'")
        elif i == "(":
            cipher.append("(")
        elif i == ")":
            cipher.append(")")
        elif i == "-":
            cipher.append("-")
        elif i == "_":
            cipher.append("_")
        elif i == ".":
            cipher.append(".")
        elif i == "?":
            cipher.append("?")
        elif i == "!":
            cipher.append("!")
        elif i == ",":
            cipher.append(",")
        elif i in numbers:
            cipher.append(f"{i}")
        elif i.isupper():
            j = Alphabet.index(i)
            index = ((j + 1)*coef + const) % 26
            cipher.append(Alphabet[index - 1])
        else:
            j = alphabet.index(i)
            index = ((j + 1)*coef + const) % 26
            cipher.append(alphabet[index - 1])
    encrypted = "".join(cipher)
    print(f"\n{encrypted}")
    f = open("encrypted_file", "a")
    f.write(f"{encrypted}")
    file.close()
    f.close()

encrypting(txt)