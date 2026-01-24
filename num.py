# Initial dictionary of number words to their numeric values
VALUES = {
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
    "quadrillion": 1000000000000000
}

# Large scales that reset "current" group
SCALES = ["thousand", "million", "billion", "trillion", "quadrillion"]

def convert(text):
    if not text:
        raise ValueError("The input string is empty.")

    words = text.lower().strip().replace("-", " ").split()
    words = [word for word in words if word != "and"]
    
    total = 0
    current_group = 0
    negative = False

    if words[0] == "minus":
        negative = True
        words.pop(0)
        if not words:
            raise ValueError("The word 'minus' must be followed by a number.")

    for word in words:
        if word not in VALUES:
            raise KeyError(f"The word '{word}' is not recognized.")

        value = VALUES[word]

        if word == "hundred":
            current_group *= value
        elif word in SCALES:
            total += (current_group * value)
            current_group = 0
        else:
            current_group += value

    result = total + current_group
    return -result if negative else result

def main():
    try:
        user_input = input("String: ")
        number = convert(user_input)
        print(f"Number: {number:,}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()