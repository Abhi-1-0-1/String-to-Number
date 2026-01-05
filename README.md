# String-to-Number Converter

A Python script that converts English word representations of numbers (e.g., "one million two hundred thousand") into formatted integers (e.g., 1,200,000).

## Features

* **Large Number Support:** Handles values from zero up to quadrillions.
* **Negative Numbers:** Supports the "minus" prefix.
* **Natural Language:** Correctly ignores the word "and" (e.g., "one hundred and five" becomes 105).
* **Readable Output:** Automatically formats results with commas for clarity.
* **Robust Error Handling:** Uses `try-except` blocks to catch typos, empty inputs, and logic errors.

## How It Works

The script processes input through four main stages:
1.  **Cleaning:** Lowercases text and removes the word "and".
2.  **Validation:** Checks if words exist in the dictionary and handles the "minus" sign.
3.  **Segmentation:** Splits the input into chunks based on large multiples (thousand, million, etc.).
4.  **Calculation:** Multiplies and sums the segments to produce the final numeric value.

## Error Handling

The script includes specific feedback for common user errors:

| Error Type | Trigger | Message Example |
| :--- | :--- | :--- |
| **KeyError** | Typos or unknown words | `Input Error: 'The word 'eleventy' is not recognized...'` |
| **ValueError** | Empty input | `Value Error: The input string is empty.` |
| **ValueError** | Leading 'minus' with no number | `Value Error: The word 'minus' must be followed by a number.` |

## Usage

1. Run the script:
   ```bash
   python converter.py
