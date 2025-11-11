from hospital import Hospital

def main():
    hospital = Hospital()

    while True:
        print("\n🏥 Hospital Management System")
        print("1. Add Doctor")
        print("2. Register Patient")
        print("3. Book Appointment")
        print("4. Show All Doctors")
        print("5. Show All Appointments")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Doctor Name: ")
            specialization = input("Specialization: ")
            timings = input("Available Timings: ")
            hospital.add_doctor(name, specialization, timings)

        elif choice == "2":
            name = input("Patient Name: ")
            age = int(input("Age: "))
            disease = input("Disease Description: ")
            hospital.register_patient(name, age, disease)

        elif choice == "3":
            patient_name = input("Patient Name: ")
            doctor_name = input("Doctor Name: ")
            hospital.book_appointment(patient_name, doctor_name)

        elif choice == "4":
            hospital.show_doctors()

        elif choice == "5":
            hospital.show_appointments()

        elif choice == "6":
            print("👋 Exiting system. Stay healthy!")
            break

        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
