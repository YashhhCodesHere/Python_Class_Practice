#  If two strings are anagrams:-
#  which means that the two strings contain the same characters in the same quantity but in a different order.

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

def check_anagram(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        print("The strings are anagrams!")
    else:
        print("The strings are not anagrams!")

check_anagram(s1, s2 )

# Another method to do the same:-

def check_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    count = [0] * 26
    for i in range(len(str1)):
        count[ord(str1[i]) - ord('a')] += 1
        count[ord(str2[i]) - ord('a')] -= 1
    for c in count:
        if c != 0:
            return False
    return True

if check_anagram(s1, s2):
    print("The strings are anagrams!")
else:
    print("The strings are not anagrams!")

