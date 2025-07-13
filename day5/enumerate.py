text = "A quick brown fox jumps over the lazy dog"
count_char = text.count('o')
print(f"Number of occurrences of 'o': {count_char}")
keep_index_of_o = []
for index, char in enumerate(text):
    if char == 'o':
        keep_index_of_o += [index]
        print(f"Found 'o' at index: {index}")
    print(f"Index: {index}, Character: '{char}'")
print("Total number of characters:", len(text))
print("Indices of 'o':", keep_index_of_o)