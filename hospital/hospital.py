class Doctor:
    def __init__(self, name, specialization, timings):
        self.name = name
        self.specialization = specialization
        self.timings = timings

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization}) - Available: {self.timings}"


class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Disease: {self.disease}"


class Appointment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor

    def __str__(self):
        return f"Appointment: {self.patient.name} with Dr. {self.doctor.name} ({self.doctor.specialization})"


class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, name, specialization, timings):
        self.doctors.append(Doctor(name, specialization, timings))

    def register_patient(self, name, age, disease):
        self.patients.append(Patient(name, age, disease))

    def book_appointment(self, patient_name, doctor_name):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)
        if patient and doctor:
            self.appointments.append(Appointment(patient, doctor))
            print("✅ Appointment booked successfully.")
        else:
            print("❌ Patient or Doctor not found.")

    def show_doctors(self):
        print("\n👨‍⚕️ List of Doctors:")
        for doc in self.doctors:
            print("-", doc)

    def show_appointments(self):
        print("\n📅 Appointments:")
        for appt in self.appointments:
            print("-", appt)
