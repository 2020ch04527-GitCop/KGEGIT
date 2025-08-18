import string
import re
from collections import Counter
# Assignment 2 file
# This Python script contains a collection of utility functions for common programming tasks,
# such as string analysis, mathematical computations, and list processing.
# Each function is designed to perform a specific operation, and example usages are provided at the end.

def char_frequency(s, ch):
    """Returns the frequency of character `ch` in string `s`."""
    return s.count(ch)

def count_vowels(s):
    """Counts the number of vowels in the string `s`."""
    return sum(1 for c in s.lower() if c in 'aeiou')

def numbers_divisible_by(n, start, end):
    """Returns a list of numbers divisible by `n` in the range [start, end]."""
    return [i for i in range(start, end+1) if i % n == 0]

def factorial_recursive(n):
    """Calculates the factorial of `n` using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    """Calculates the factorial of `n` using iteration."""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def fibonacci_recursive(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    """Returns a list of the first `n` Fibonacci numbers using iteration."""
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def welcome_name(name, name_list):
    """Returns a welcome message if `name` is in `name_list`, otherwise a goodbye message."""
    return "Welcome" if name in name_list else "See you next time"

def is_prime(n):
    """Checks if `n` is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Returns a list of prime numbers in the range [start, end]."""
    return [i for i in range(start, end+1) if is_prime(i)]

def is_perfect(n):
    """Checks if `n` is a perfect number."""
    return n == sum(i for i in range(1, n) if n % i == 0)

def perfect_numbers_in_range(start, end):
    """Returns a list of perfect numbers in the range [start, end]."""
    return [i for i in range(start, end+1) if is_perfect(i)]

def is_palindrome(n):
    """Checks if the integer `n` is a palindrome."""
    s = str(n)
    return s == s[::-1]

def is_pangram(sentence):
    """Checks if the given sentence is a pangram (contains every letter of the alphabet)."""
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))

def is_anagram(s1, s2):
    """Checks if strings `s1` and `s2` are anagrams of each other."""
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def char_frequencies(s):
    """Returns a dictionary of character frequencies in string `s`."""
    return dict(Counter(s))

def is_armstrong(n):
    """Checks if `n` is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return n == sum(d**len(digits) for d in digits)

def armstrong_numbers_in_range(start, end):
    """Returns a list of Armstrong numbers in the range [start, end]."""
    return [i for i in range(start, end+1) if is_armstrong(i)]

def sieve_of_eratosthenes(n):
    """Returns a list of all prime numbers up to `n` using the Sieve of Eratosthenes."""
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def primes_fast(start, end):
    """Returns a list of prime numbers in the range [start, end] using an optimized sieve."""
    primes = sieve_of_eratosthenes(end)
    return [p for p in primes if p >= start]

def word_frequencies(sentence):
    """Returns a dictionary of word frequencies in the given sentence."""
    words = sentence.split()
    return dict(Counter(words))

def reverse_each_word(sentence):
    """Returns the sentence with each word reversed."""
    return ' '.join(word[::-1] for word in sentence.split())

def check_password(password):
    """Checks if the password meets criteria: uppercase, lowercase, digit, and special character."""
    return (bool(re.search(r'[A-Z]', password)) and
            bool(re.search(r'[a-z]', password)) and
            bool(re.search(r'[0-9]', password)) and
            bool(re.search(r'[^A-Za-z0-9]', password)))

def atoi(s):
    """Converts string `s` to an integer, returns None if conversion fails."""
    try:
        return int(s)
    except ValueError:
        return None
    return (bool(re.search(r'[A-Z]', password)) and
            bool(re.search(r'[a-z]', password)) and
            bool(re.search(r'[0-9]', password)) and
            bool(re.search(r'[^A-Za-z0-9]', password)))

def atoi(s):
    """Converts string `s` to an integer, returns None if conversion fails."""
    try:
        return int(s)
    except ValueError:
        return None


# Example function calls
print("Frequency of 'a' in 'banana':", char_frequency('banana', 'a'))
print("Number of vowels in 'hello world':", count_vowels('hello world'))
print("Numbers divisible by 3 in range 1-20:", numbers_divisible_by(3, 1, 20))
print("Factorial of 5 (recursive):", factorial_recursive(5))
print("Factorial of 5 (iterative):", factorial_iterative(5))
print("Fibonacci series (recursive, first 7):", [fibonacci_recursive(i) for i in range(7)])
print("Fibonacci series (iterative, first 7):", fibonacci_iterative(7))
print(welcome_name("Alice", ["Bob", "Alice", "Eve"]))
print("Is 17 prime?", is_prime(17))
print("Primes in range 10-30:", primes_in_range(10, 30))
print("Is 28 perfect?", is_perfect(28))
print("Perfect numbers in range 1-1000:", perfect_numbers_in_range(1, 1000))
print("Is 121 palindrome?", is_palindrome(121))
print("Is 'The quick brown fox jumps over the lazy dog' a pangram?", is_pangram("The quick brown fox jumps over the lazy dog"))
print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))
print("Character frequencies in 'hello':", char_frequencies("hello"))
print("Is 153 Armstrong?", is_armstrong(153))
print("Armstrong numbers in range 1-1000:", armstrong_numbers_in_range(1, 1000))
print("Primes up to 50 (Sieve):", sieve_of_eratosthenes(50))
print("Primes in range 100-150 (fast):", primes_fast(100, 150))
print("Word frequencies in 'hello world hello':", word_frequencies("hello world hello"))
print("Reverse each word in 'hello world':", reverse_each_word("hello world"))
print("Is 'Password1!' a valid password?", check_password("Password1!"))
print("Convert '1234' to int:", atoi("1234"))