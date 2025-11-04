"""
Lab 3.3 – Operator Frequency Counter

Goals:
- Practice using strings and dictionaries.
- Count character frequencies in user-provided text.

Instructions:
1. Ask the user for an arithmetic expression, e.g. "3 + 5 * (2 - 1) + 7 / 2".
2. Count how many times each operator occurs:
   +  -  *  /  (  )
3. Store counts in a dictionary.
4. Print the result.
"""

# Get input from the user
expression = input("Enter an arithmetic expression: ")

# Define possible operator symbols
operators = ["+", "-", "*", "/", "(", ")"]

# Initialize frequency dictionary
operator_counts = {op: 0 for op in operators}

# Count operator occurrences
for char in expression:
    if char in operator_counts:
        operator_counts[char] += 1

# Print results
print("Operator counts:")
for op in operators:
    print(f" {op}: {operator_counts[op]}")
