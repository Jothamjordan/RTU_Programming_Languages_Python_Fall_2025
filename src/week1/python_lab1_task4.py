"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re
from typing import List, Optional, Tuple


def count_characters(text: str) -> int:
    """Count non-space characters in a string (exclude all whitespace)."""
    return sum(1 for ch in text if not ch.isspace())


def count_words(text: str) -> int:
    """Count number of words in a string using whitespace splitting."""
    return len(text.split())


def extract_numbers(text: str) -> List[int]:
    """Return list of integers found in text (handles optional leading -)."""
    matches = re.findall(r"-?\d+", text)
    return [int(m) for m in matches]


def analyze_text(text: str) -> Tuple[int, int, List[int], int, Optional[float]]:
    """Perform text-based arithmetic analysis and return:
    (non_space_chars, word_count, numbers_list, total, average_or_None)
    """
    chars = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)
    average = (total / len(numbers)) if numbers else None
    return chars, words, numbers, total, average


if __name__ == "__main__":
    text = input("Enter text: ")
    chars, words, numbers, total, average = analyze_text(text)
