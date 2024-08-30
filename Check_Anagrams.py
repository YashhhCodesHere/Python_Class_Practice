s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

def check_anagram(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        print("The strings are anagrams!")
    else:
        print("The strings are not anagrams!")

check_anagram(s1, s2 )