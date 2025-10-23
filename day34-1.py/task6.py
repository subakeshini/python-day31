# Word Frequency Counter

# Step 1: Get input from the user
sentence = input("Enter a sentence: ")

# Step 2: Split the sentence into words
words = sentence.split()

# Step 3: Create a dictionary to store word frequencies
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Step 4: Display the result
print("\nWord Frequency Count:")
for i, (word, count) in enumerate(frequency.items(), start=1):
    print(f"{i}. {word} -> {count}")
