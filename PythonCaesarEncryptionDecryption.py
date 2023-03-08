string = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpit ghlxiwiwtxgqadds"
# Declare a dictionary mapping the old letters to the new letters
mapping = {
    "a": "L",
    "b": "M",
    "c": "N",
    "d": "O",
    "e": "P", 
    "f": "Q",
    "g": "R",
    "h": "S",
    "i": "T",
    "j": "U",
    "k": "V",
    "l": "W",
    "m": "X",
    "n": "Y",
    "o": "Z",
    "p": "A",
    "q": "B",
    "r": "C",
    "s": "D",
    "t": "E",
    "u": "F",
    "v": "G",
    "w": "H",
    "x": "I",
    "y": "J",
    "z": "K"
}

# Iterate through the string and replace each letter using the mapping
result = ""
for letter in string:
    if letter in mapping:
        result += mapping[letter]
    else:
        result += letter

# Print the original msg if you wanna compare results 
print(string)
# Print the result
print(result)
