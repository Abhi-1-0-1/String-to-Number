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
    "trillion": 1000000000000,
    "quadrillion": 1000000000000000,

    "minus": -1
}

negative = False

try:
    # Take input from user and clean it
    n = input("String: ").lower().strip()
    
    # Error Handling: Check if input is empty
    if not n:
        raise ValueError("The input string is empty. Please enter a number in words.")

    words = n.split()

    # Clean "and" from the list
    words = [word for word in words if word != "and"]

    # Handle negative numbers
    if words[0] == "minus":
        negative = True
        words.pop(0)
        # Error Handling: Check if "minus" is followed by a number
        if not words:
            raise ValueError("The word 'minus' must be followed by a number.")

    # Split the words by large number multiples    
    split_by_multiples = []
    current_segment = []

    for i in words:
        # Error Handling: Check if word exists in our dictionary
        if i not in values:
            raise KeyError(f"The word '{i}' is not a recognized number or is formatted incorrectly.")
            
        current_segment.append(i)
        if i in ["thousand", "million", "billion", "trillion", "quadrillion"]:
            split_by_multiples.append(current_segment)
            current_segment = []
            
    # Append the remaining words
    if current_segment:
        split_by_multiples.append(current_segment)

    # Calculate the numeric value for each segment
    for index, segment in enumerate(split_by_multiples):
        temp = 0
        for word in segment:
            value = values[word]
            if word == "hundred":
                # If hundred is at start of segment
                if temp == 0: temp = 1
                temp *= value
            elif word in ["thousand", "million", "billion", "trillion", "quadrillion"]:
                # If multiple is at start of segment
                if temp == 0: temp = 1
                temp *= value
            else:
                temp += value

        split_by_multiples[index] = temp

    number = sum(split_by_multiples)
    number = -1*number if negative else number

    # Add commas to the number for readability
    number_with_commas = "{:,}".format(number)

    print("Number:", number_with_commas)

except KeyError as e:
    print(f"Input Error: {e}")
except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")