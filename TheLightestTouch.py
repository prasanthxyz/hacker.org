braillecodes = {
    "000000": " ",
    "100000": "a",
    "110000": "b",
    "100100": "c",
    "100110": "d",
    "100010": "e",
    "110100": "f",
    "110110": "g",
    "110010": "h",
    "010100": "i",
    "010110": "j",
    "101000": "k",
    "111000": "l",
    "101100": "m",
    "101110": "n",
    "101010": "o",
    "111100": "p",
    "111110": "q",
    "111010": "r",
    "011100": "s",
    "011110": "t",
    "101001": "u",
    "111001": "v",
    "010111": "w",
    "101101": "x",
    "101111": "y",
    "101011": "z",
}

cipher = """
 . .  .     .  ..  .  . .  .      .  .     . .  .  .. .. .  ..  .  . .  .  .. .. .  
.. ..  .        . .  ..  . ..    .  .     .   .     .  .  . .  .  .  .   .  .     . 
.              .  .   .    .        .     .  .  .. .     .     .     .     .        
"""

lines = cipher[1:-1].split("\n")
transpose = list(map(list, zip(*lines)))
chars = []
current_char = ""
for i in range(0, len(transpose), 3):
    current_char += "".join(['1' if x == '.' else '0' for x in transpose[i]])
    current_char += "".join(['1' if x == '.' else '0' for x in transpose[i+1]])
    chars.append(current_char)
    current_char = ""

for char in chars:
    print(braillecodes[char], end="")
