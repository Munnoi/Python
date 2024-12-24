# Fibonacci
class Fibonacci:
    def __init__(self) -> None:
        self.first = 0
        self.second = 1

    def fibonacci_upto_n_numbers(self, n):
        first, second = self.first, self.second
        print(first, end=' ')
        print(second, end=' ')

        for i in range(n - 2):
            third = first + second
            print(third, end=' ')
            first = second
            second = third
        print()

    def fibonacci_upto_n(self, n):
        first, second = self.first, self.second
        print(first, end=' ')
        print(second, end=' ')

        # third = 0
        while True:
            third = first + second
            if third > n:
                break
            print(third, end=' ')
            first = second
            second = third
        print()

    def definition(self):
        print("""The Fibonacci series is a sequence of numbers where each number (after the first two) is the sum of the two preceding ones. The sequence starts with 0 and 1.\nExample: 0,1,1,2,3,5,8,13,21,34,55,…
        """)

# Palindrome
class Palindrome:
    def is_palindrome(self, string):
        return string == string[::-1]
    def definition(self):
        print("""A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.\nExample: 'madam', 'racecar', 'level', 121, 12321, 1001""")

# Count vowels
class Count_vowels:
    def __init__(self) -> None:
        self.count = 0
    def count_vowels(self, string):
        count = self.count
        for char in string:
            if char in ('aeiou' or 'AEIOU'):
                count+=1
        return count
    def definition(self):
        print("Counts the number of vowels (a, e, i, o, u) in a given string")

# Sum of digits
class Sum_of_digits:
    def __init__(self) -> None:
        self.sum = 0
    def sum_of_digits(self, number):
        sum = self.sum
        while number:
            last_digit = number % 10
            sum += last_digit
            number //= 10
        return sum
    def definition(self):
        print("Takes an integer and returns the sum of its digits")

# Largest element in a list
class Largest_in_a_list:
    def largest(self, arr):
        max_el = arr[0]
        for i in range(1, len(arr)):
            if max_el < arr[i]:
                max_el = arr[i]
        return max_el
    def definition(self):
        print("Finds the largest number in a list of numbers")

# Reversing a list
class Reverse_list:
    def reverse(self, arr):
        reversed_list = [x for x in arr[::-1]]
        return reversed_list
    def definition(self):
        print("Reverses a list")

# Count occurence of an element
class Count_occurence:
    def __init__(self) -> None:
        self.count = 0
    def count_occurence(self, lst, n):
        count = self.count
        for x in lst:
            if x == n:
                count+=1
        return count
    def definition(self):
        print("Counts the occurrences of a specific element in a list")

# Temperature converter
class Temperature:
    def convert_to_c(self, temp):
        return (temp - 32) * 5 / 9
    def convert_to_f(self, temp):
        return (temp * 9 / 5) + 32
    def definition(self):
        print("Converts a temperature from Celsius to Fahrenheit and vice versa")

# Find duplicate elements
class Duplicate:
    def duplicates(self, lst):
        duplicates = []
        seen = ()
        for item in lst:
            if item in seen and item not in duplicates:
                duplicates.append(item)
            else:
                seen.add(item)
        return duplicates
    def definition(self):
        print("Finds all the duplicate elements in a list")

# Sum of natural numbers
class Sum:
    def __init__(self) -> None:
        self.sum = 0
    def sum_of_natural_nos(self, n):
        n = self.n
        for i in range(1, n+1):
            sum += i
        return sum
    def definition(self):
        print("Calculates the sum of the first n natural numbers")