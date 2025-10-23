def verify_pin(correct_pin="1234", max_attempts=3):
    attempts = max_attempts
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ").strip()
        
        if not pin.isdigit() or len(pin) != 4:
            print("⚠️ Invalid format! Please enter a 4-digit numeric PIN.")
            continue

        if pin == correct_pin:
            print("✅ Access Granted!")
            break
        else:
            attempts -= 1
            print(f"❌ Incorrect PIN! {attempts} attempts left.")
            if attempts == 0:
                print("🚫 Access Denied. Your account is locked.")
            else:
                continue
    else:
        print("🔒 Loop ended without successful login.")

# Run the system
verify_pin()
