while True:
    text = input("Enter something (type 'exit' to stop): ")
    if text.lower() == "exit":
        break
    print("You entered:", text)


i = 1
while i <= 20:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
while True:
    num = int(input("Enter a number: "))
    if num > 0:
        print("Thank you!")
        break
i = 1
while i <= 30:
    if i % 3 != 0:
        print(i)
    i += 1
import random
secret = random.randint(1, 10)
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("🎉 Correct!")
        break
correct_password = "admin123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("✅ Access Granted")
        break
correct_pin = "1234"
attempts = 3
while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("✅ Access Granted")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN! {attempts} attempts left.")
        if attempts == 0:
            print("🚫 Account Locked")
for _ in range(10):
    pass

for i in range(5):
    pass  # Logic to be added later
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully")

found = False

while True:
    word = input("Enter a word (type 'Python' to stop): ")
    if word == "Python":
        found = True
        print("✅ You entered 'Python'. Loop stopped.")
        break

# This else block runs only if the loop ends naturally (not by break)
if not found:
    print("You never entered 'Python'!")
