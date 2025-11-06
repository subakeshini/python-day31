import string

# 1. Ask the user to input a paragraph
paragraph = input("Enter a paragraph:\n")

# 2. Convert paragraph to lowercase and remove punctuation
cleaned_paragraph = paragraph.lower().translate(str.maketrans("", "", string.punctuation))

# 3. Convert to a set of unique words
words = set(cleaned_paragraph.split())

# 4. Define a frozen set of common words
common_words = frozenset({"is", "a", "the", "and", "to", "of", "in"})

# 5. Remove common words from the unique words set
unique_words = words.difference(common_words)

# 6. Display the total and the unique words
print(f"\n🔢 Total Unique Words (excluding common words): {len(unique_words)}")
print("📝 Unique Words:")
for word in sorted(unique_words):
    print(f"- {word}")
