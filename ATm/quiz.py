import csv
import os

FILENAME = "scores.csv"

def add_score():
    """Adds a new quiz score to the CSV file."""
    name = input("👤 Enter student name: ").strip()
    subject = input("📚 Enter subject: ").strip()
    try:
        score = float(input("🎯 Enter score: "))
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, subject, score])
        print("✅ Score added successfully!")
    except ValueError:
        print("❌ Invalid score. Please enter a numeric value.")

def view_scores():
    """Displays all quiz scores from the CSV file."""
    if not os.path.exists(FILENAME):
        print("\n📭 No scores recorded yet.")
        return
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        scores = list(reader)
        if not scores:
            print("\n📭 No scores recorded yet.")
            return
        print("\n📋 Quiz Score Records:")
        print(f"{'Name':<15}{'Subject':<15}{'Score'}")
        print("-" * 35)
        for row in scores:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]}")

def search_score():
    """Searches for a student's score by name."""
    search_name = input("🔍 Enter student name to search: ").strip().lower()
    found = False
    if not os.path.exists(FILENAME):
        print("\n📂 No score records found.")
        return
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].strip().lower() == search_name:
                print(f"\n✅ Found: Name: {row[0]}, Subject: {row[1]}, Score: {row[2]}")
                found = True
    if not found:
        print("❌ Student not found!")

# Main program loop
def run_quiz_score_manager():
    while True:
        print("\n📝 Quiz Score Manager Menu")
        print("1. Add Score")
        print("2. View All Scores")
        print("3. Search Score by Name")
        print("4. Exit")
        choice = input("🔢 Enter your choice (1-4): ").strip()
        if choice == "1":
            add_score()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            search_score()
        elif choice == "4":
            print("👋 Goodbye! Your scores are saved.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the manager
run_quiz_score_manager()
