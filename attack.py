import collections

txt = str(input(" File address please: "))
print("\nChoose a long text to crack correctly, these are English frequencies and if you do not give a long message the errors must be more!\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
frequency = "etaoinshrdlcumwfgypbvkjxqz"
cracked = []

def crack(b):
    file = open(f"{b}", "r")
    content = file.read()
    key = {}
    content = content.replace(" ", "")
    content = content.replace("\n", "")
    content = content.lower()
    frequent_letters = collections.Counter(content).most_common()
    index = 0
    for i in frequent_letters:
        if i[0] in alphabet:
            key[frequency[index]] = i[0]
            index += 1 
    return key





print(crack(txt))