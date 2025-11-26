# Initial dictionary of number words to their numeric values
values = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000,
    "billion": 1000000000,
    "trillion": 1000000000000
}

#Take input from user and clean it
n = input("String: ").lower().strip()
words = n.split()
words = [word for word in words if word != "and"]
if words[0] in ["minus", "negative"]:
    words = words[1:]
    negative = True
else:
    negative = False
# Split the words by large number multiples    
split_by_multiples = []
for i in words:
    if i in list(values.keys())[list(values.keys()).index("thousand"):]:
        split_by_multiples.append(words[:words.index(i)+1])
        words = words[words.index(i)+1:]

split_by_multiples.append(words)

# Calculate the numeric value for each segment
for index, segment in enumerate(split_by_multiples):
    temp = 0
    for word in segment:
        value = values[word]
        if word in list(values.keys())[list(values.keys()).index("hundred"):]:
            temp *= value
        else:
            temp += value
    split_by_multiples[index] = temp
number = sum(split_by_multiples)

# Add commas to the number for readability
number_with_commas = "{:,}".format(number)
if negative:
    number_with_commas = "-" + number_with_commas
print("Number:", number_with_commas)