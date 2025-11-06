# Contact Book Dictionary
contacts = {}

# 1. Add a new contact
def add_contact(name, phone, email):
    if name in contacts:
        print(f"⚠️ Contact '{name}' already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"✅ Contact '{name}' added successfully!")

# 2. Update contact details
def update_contact(name, key, value):
    if name in contacts:
        if key in contacts[name]:
            contacts[name][key] = value
            print(f"🔄 Contact '{name}' updated successfully!")
        else:
            print(f"⚠️ Invalid field '{key}'. Use 'phone' or 'email'.")
    else:
        print(f"❌ Contact '{name}' not found.")

# 3. Delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print(f"❌ Contact '{name}' not found.")

# 4. Search for a contact
def search_contact(name):
    if name in contacts:
        print(f"\n🔍 Contact Found:\nName: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"❌ Contact '{name}' not found.")

# 5. Display all contacts
def display_contacts():
    if contacts:
        print("\n📇 All Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("📭 No contacts available.")

# Sample Execution
add_contact("John Doe", "9876543210", "john@example.com")
add_contact("Alice Smith", "9123456789", "alice@example.com")
update_contact("John Doe", "phone", "9999999999")
search_contact("Alice Smith")
delete_contact("John Doe")
display_contacts()
