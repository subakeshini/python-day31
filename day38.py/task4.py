# Frozen set of strong passwords (Immutable)
strong_passwords = frozenset({"P@ssw0rd123", "Secure#456", "Python$789"})

# Function to check if a password is strong
def check_password(password):
    if password in strong_passwords:
        print("✅ Strong Password!")
    else:
        print("❌ Weak Password! Consider using one of these:")
        for pwd in strong_passwords:
            print(f"- {pwd}")

# Function to generate a new set of suggested passwords
def suggest_passwords():
    additional_passwords = {"Safe@111", "Strong$222"}
    new_suggestions = strong_passwords.union(additional_passwords)  # Join sets
    print("\n💡 Suggested Strong Passwords:")
    for pwd in new_suggestions:
        print(f"- {pwd}")

# Sample Execution
check_password("P@ssw0rd123")  # Strong
check_password("weakpass")     # Weak
suggest_passwords()
