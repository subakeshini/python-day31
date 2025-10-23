for char in "PYTHON":
    print(char)

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed string:", reversed_text)


for i in range(1, 21):
    print(i)

for i in range(2, 51, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break

for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)

for i in range(1, 11):
    if i == 5:
        pass
    print(i)

for i in range(1, 11):
    print(i)
else:
    print("Loop finished successfully")

for index, char in enumerate("HELLO"):
    print(f"Index {index}: {char}")

sentence = input("Enter a sentence: ")
words = sentence.split()
for index, word in enumerate(words, start=1):
    print(f"{index}. {word}")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-----")


import time
start = time.time()
while time.time() - start < 5:
    print("Hello, World!")

