# ----------------------------------TEXT TO BRAILLE---------------------------------- #

# Variables
braille = {}
converted = ""
extra = ""


# Open file
with open("braille") as file:
    data = file.read()


# Add data to braille dictionary
for i in data.split():
    braille[i[0]] = i[2]


# ---------------------------------BRAILLE CONVERTER--------------------------------- #
# User input
words = input("Type your text:\n> ").lower()


# Convert
for i in words:
    if i in braille:
        converted += (braille[i])
    elif i == " ":
        converted += "  "
    elif i not in braille:
        extra += i


# Print converted text
if extra:
    print(f"{converted}\nUnable to convert: {extra}")
else:
    print(converted)
