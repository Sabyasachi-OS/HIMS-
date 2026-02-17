markdown
# 🏥 Hospital Information Management System (HIMS)

A simple yet effective Python-based Hospital Information Management System that helps healthcare facilities manage patient records, doctor information, and appointments efficiently using file-based storage.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Data Storage](#data-storage)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Patient Management
- ➕ Add new patients with complete details
- 👀 View all patient records
- 📝 Store patient information including ID, name, age, gender, and contact

### Doctor Management  
- 👨‍⚕️ Add new doctors with specialization
- 📋 View all doctor records
- 🔍 Store doctor details including ID, name, specialization, and contact

### Appointment System
- 📅 Book appointments between patients and doctors
- ⏰ Schedule appointments with date and time
- 🔄 View all appointments with patient and doctor names
- ✅ Automatic validation for existing patients and doctors

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Pickle Module** - Data serialization and storage
- **OS Module** - File system operations

## 📥 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/HIMS-Python.git
cd HIMS-Python
Ensure Python is installed

bash
python --version
Make sure you have Python 3.6 or higher installed.

Run the application

bash
python "HIMS PYTHON.py"
🚀 Usage
Start the program

bash
python "HIMS PYTHON.py"
Navigate the main menu

text
=== Hospital Information Management System ===
1. Add Patient
2. Add Doctor
3. Book Appointment
4. View Patients
5. View Doctors
6. View Appointments
7. Exit
Add a Patient

Select option 1

Enter Patient ID (e.g., P001)

Enter Patient Name

Enter Patient Age

Enter Patient Gender

Enter Contact Number

Add a Doctor

Select option 2

Enter Doctor ID (e.g., D001)

Enter Doctor Name

Enter Specialization

Enter Contact Number

Book an Appointment

Select option 3

Choose Patient ID from the displayed list

Choose Doctor ID from the displayed list

Enter Date (DD-MM-YYYY)

Enter Time (HH:MM)

📁 File Structure
text
HIMS-Python/
│
├── HIMS PYTHON.py          # Main application file
├── patients.pkl             # Auto-generated patient database
├── doctors.pkl              # Auto-generated doctor database
├── appointments.pkl         # Auto-generated appointment database
├── README.md                # Project documentation
└── .gitignore               # Git ignore file
💾 Data Storage
The system uses Python's pickle module for data persistence:

patients.pkl - Stores list of patient dictionaries

doctors.pkl - Stores list of doctor dictionaries

appointments.pkl - Stores list of appointment dictionaries

Data Structure Examples
Patient Record:

python
{
    "id": "P001",
    "name": "John Doe",
    "age": "30",
    "gender": "Male",
    "contact": "1234567890"
}
Doctor Record:

python
{
    "id": "D001",
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "contact": "9876543210"
}
Appointment Record:

python
{
    "patient_id": "P001",
    "doctor_id": "D001",
    "date": "15-03-2024",
    "time": "14:30"
}
