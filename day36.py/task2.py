# 🎉 Fun String Manipulator Tool

# Taking user input
sentence = input("Enter a sentence: ").strip()

# Performing string manipulations
uppercase = sentence.upper()
lowercase = sentence.lower()
first_char = sentence[0]
last_char = sentence[-1]
reversed_sentence = sentence[::-1]
repeated_sentence = sentence * 3

# Formatting a new string using the first word
formatted_output = f"Learning {sentence.split()[0]} is really FUN!"

# Displaying results
result = f"""
Fun String Manipulator  ----------------------------
Original Sentence  : {sentence}
Uppercase          : {uppercase}
Lowercase          : {lowercase}
First Character    : {first_char}
Last Character     : {last_char}
Reversed Sentence  : {reversed_sentence}
Repeated Sentence  : {repeated_sentence}
Formatted Output   : {formatted_output}
----------------------------
"""

print(result)
