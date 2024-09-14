def sort_hyphenated_words(input_sequence):
    words = input_sequence.split('-')
    words.sort()
    sorted_sequence = '-'.join(words)
    print("Sorted sequence:", sorted_sequence)

input_sequence = input("Enter a hyphen-separated sequence of words: ")
sort_hyphenated_words(input_sequence)