a = int(input(" Taking the argument of coeff: "))
c = int(input(" Taking the argument of const: "))
txt = str(input(" What is the encrypted file address: "))
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
plain = []
if a == 1:
    g = 1
elif a == 3:
    g = 9
elif a == 5:
    g = 21
elif a == 7:
    g = 15
elif a == 9:
    g = 3
elif a == 11:
    g = 19
elif a == 15:
    g = 7
elif a == 17:
    g = 23
elif a == 19:
    g = 11
elif a == 21:
    g = 5
elif a == 23:
    g = 17
elif a == 25:
    g = 25  

def decrypting(b):
    file = open(f"{b}", "r")
    content = file.read()
    for i in content:
        if i == " ":
            plain.append(" ")
        elif i == "\n":
            plain.append("\n")
        elif i == ".":
            plain.append(".")
        elif i == "?":
            plain.append("?")
        elif i == "!":
            plain.append("!")
        elif i == ",":
            plain.append(",")
        else:
            j = alphabet.index(i)
            index = (((j+1) - c) *g) % 26
            plain.append(alphabet[index - 1])
    decrypted = "".join(plain)
    print(f"\n{decrypted}")
    file.close()

print("remember that the coeff you choose should be coprime with 26!")
decrypting(txt)
