#1 Write a Python program to calculate the total number of Vowels and count of each individual Vowel A,E,I,O,U in the string 'Guvi Geeks Network Private Limited'

def count_vowels(s):
    vowels = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    total_vowels = 0
    s = s.upper()

    for char in s:
        if char in vowels:
            vowels[char] += 1
            total_vowels += 1

    return total_vowels, vowels

string = "Guvi Geeks Network Private Limited"
total_vowels, vowel_counts = count_vowels(string)

print("Total number of vowels:", total_vowels)
print("Count of each vowel:", vowel_counts)

#2 Create a Pyramid of Number from 1 to 20 using For Loop

def print_pyramid(n):
    num = 1
    for i in range(1, n+1):
     for j in range(i):
        if num <= n:
             	print(num, end=" ")
             	num += 1
    print()

print_pyramid(20)

#3

#4 write a program that takes a string and return the number of unique characters in it

def unique_characters(input_string):
    characters = set(input_string)
    return len(characters)

input_string = "hello world"
print(unique_characters(input_string))

#5 Write a program that takes a string and return  True if it is a palindrome, False otherwise.

def Palindrome(input_string):
    str1= list(input_string)
    str2= str1[::-1]

    if str1 == str2:
        print("True")
    else:
        print("False")

input_string= "weffeq"
Palindrome(input_string)

#6 Write a Program that takes a two strings and return the longest common substring between them.

def longest_common_substring(str1, str2):
    max_length = 0
    longest_substring = ""

    len1, len2 = len(str1), len(str2)

    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ""

            while (i + lcs_temp < len1) and (j + lcs_temp < len2) and (str1[i + lcs_temp] == str2[j + lcs_temp]):
                match += str1[i + lcs_temp]
                lcs_temp += 1

            if lcs_temp > max_length:
                max_length = lcs_temp
                longest_substring = match

    return longest_substring

str1 = "abcdefq"
str2 = "zcdemfsw"
print(longest_common_substring(str1, str2))  # Output: "cde"

#7 Write a program that takes a string and return the most frequent character in it.

def most_frequent_character(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    most_frequent = max(frequency, key=frequency.get)
    return most_frequent

string = "Guvi Geeks Network Private Limited"
most_frequent = most_frequent_character(string)

print("Most frequent character:", most_frequent)

#8 Write a program that takes a string and return True is it is anagram of another string,False otherwise

def are_anagrams(s1, s2):
 	return sorted(s1) == sorted(s2)

s1 = "listen"
s2 = "silent"
result = are_anagrams(s1, s2)

print("Are anagrams:", result)

#9 Write a program that takes a string and return the number of words in it.

def Numbers(input_string):
    str=input_string.split()
    return len(str)

input_string= "Hi Shaily"
result=Numbers(input_string)
print(result)