import pickle
import os

# File names for storing data
PATIENT_FILE = "patients.pkl"
DOCTOR_FILE = "doctors.pkl"
APPOINTMENT_FILE = "appointments.pkl"


# Helper function to load data
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    else:
        return []


# Helper function to save data
def save_data(file_name, data):
    with open(file_name, "wb") as f:
        pickle.dump(data, f)


# Add a patient
def add_patient():
    patients = load_data(PATIENT_FILE)
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    gender = input("Enter Patient Gender: ")
    contact = input("Enter Contact Number: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact
    }

    patients.append(patient)
    save_data(PATIENT_FILE, patients)
    print("Patient added successfully!")


# Add a doctor
def add_doctor():
    doctors = load_data(DOCTOR_FILE)
    doctor_id = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    contact = input("Enter Contact Number: ")

    doctor = {
        "id": doctor_id,
        "name": name,
        "specialization": specialization,
        "contact": contact
    }

    doctors.append(doctor)
    save_data(DOCTOR_FILE, doctors)
    print("Doctor added successfully!")


# Book an appointment
def book_appointment():
    appointments = load_data(APPOINTMENT_FILE)
    patients = load_data(PATIENT_FILE)
    doctors = load_data(DOCTOR_FILE)

    if not patients or not doctors:
        print("Patients or Doctors data missing. Cannot book appointment.")
        return

    print("\nPatients List:")
    for p in patients:
        print(f"{p['id']}: {p['name']}")

    print("\nDoctors List:")
    for d in doctors:
        print(f"{d['id']}: {d['name']} ({d['specialization']})")

    patient_id = input("Enter Patient ID for Appointment: ")
    doctor_id = input("Enter Doctor ID for Appointment: ")
    date = input("Enter Appointment Date (DD-MM-YYYY): ")
    time = input("Enter Appointment Time (HH:MM): ")

    appointment = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    save_data(APPOINTMENT_FILE, appointments)
    print("Appointment booked successfully!")


# View all patients
def view_patients():
    patients = load_data(PATIENT_FILE)
    if not patients:
        print("No patients found!")
        return
    print("\n--- Patients List ---")
    for p in patients:
        print(f"ID: {p['id']}, Name: {p['name']}, Age: {p['age']}, Gender: {p['gender']}, Contact: {p['contact']}")


# View all doctors
def view_doctors():
    doctors = load_data(DOCTOR_FILE)
    if not doctors:
        print("No doctors found!")
        return
    print("\n--- Doctors List ---")
    for d in doctors:
        print(f"ID: {d['id']}, Name: {d['name']}, Specialization: {d['specialization']}, Contact: {d['contact']}")


# View all appointments
def view_appointments():
    appointments = load_data(APPOINTMENT_FILE)
    patients = {p['id']: p['name'] for p in load_data(PATIENT_FILE)}
    doctors = {d['id']: d['name'] for d in load_data(DOCTOR_FILE)}

    if not appointments:
        print("No appointments found!")
        return

    print("\n--- Appointments List ---")
    for a in appointments:
        patient_name = patients.get(a['patient_id'], "Unknown")
        doctor_name = doctors.get(a['doctor_id'], "Unknown")
        print(f"Patient: {patient_name}, Doctor: {doctor_name}, Date: {a['date']}, Time: {a['time']}")


# Main menu
def main_menu():
    while True:
        print("\n=== Hospital Information Management System ===")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            add_doctor()
        elif choice == "3":
            book_appointment()
        elif choice == "4":
            view_patients()
        elif choice == "5":
            view_doctors()
        elif choice == "6":
            view_appointments()
        elif choice == "7":
            print("Exiting HIMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
