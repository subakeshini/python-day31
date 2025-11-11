# Custom Exception for full booking
class BookingFullError(Exception):
    """Raised when no seats are available for booking."""
    pass

# Sample seat availability by type
seats = {
    "Sleeper": 3,
    "AC": 2,
    "General": 5
}

# Ticket database
tickets = []

def display_seats():
    print("\n🪑 Available Seats:")
    for seat_type, count in seats.items():
        print(f"{seat_type}: {count} seats")

def book_ticket():
    try:
        name = input("👤 Enter passenger name: ").strip()
        if not name:
            raise ValueError("Passenger name cannot be empty.")
        destination = input("📍 Enter destination: ").strip()
        display_seats()
        seat_type = input("🎫 Choose seat type (Sleeper/AC/General): ").strip().title()
        if seat_type not in seats:
            raise IndexError("Invalid seat type selected.")
        if seats[seat_type] <= 0:
            raise BookingFullError(f"No {seat_type} seats available.")
        # Book ticket
        ticket = {"Name": name, "Destination": destination, "Seat": seat_type}
        tickets.append(ticket)
        seats[seat_type] -= 1
        print(f"✅ Ticket booked successfully for {name} to {destination} in {seat_type} class.")
    except ValueError as e:
        print("❌ Error:", e)
    except IndexError as e:
        print("❌ Error:", e)
    except BookingFullError as e:
        print("❌ Error:", e)

def cancel_ticket():
    if not tickets:
        print("📭 No tickets to cancel.")
        return
    print("\n🗑️ Booked Tickets:")
    for i, ticket in enumerate(tickets, start=1):
        print(f"{i}. {ticket['Name']} - {ticket['Destination']} ({ticket['Seat']})")
    try:
        index = int(input("Enter ticket number to cancel: "))
        if index < 1 or index > len(tickets):
            raise IndexError("Invalid ticket number.")
        canceled = tickets.pop(index - 1)
        seats[canceled["Seat"]] += 1
        print(f"✅ Ticket for {canceled['Name']} canceled successfully.")
    except ValueError:
        print("❌ Please enter a valid number.")
    except IndexError as e:
        print("❌ Error:", e)

def view_tickets():
    if not tickets:
        print("📭 No tickets booked yet.")
    else:
        print("\n📋 Booked Tickets:")
        for i, ticket in enumerate(tickets, start=1):
            print(f"{i}. Name: {ticket['Name']}, Destination: {ticket['Destination']}, Seat: {ticket['Seat']}")

# Main program loop
def run_booking_system():
    while True:
        print("\n🚆 Railway Ticket Booking System")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Tickets")
        print("4. Exit")
        choice = input("🔢 Enter your choice (1-4): ").strip()
        if choice == "1":
            book_ticket()
        elif choice == "2":
            cancel_ticket()
        elif choice == "3":
            view_tickets()
        elif choice == "4":
            print("👋 Thank you for using the Railway Booking System!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the system
run_booking_system()
