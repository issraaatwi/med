class Patient:
    def __init__(self, first_name, middle_name, family_name, gender, primary_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.gender = gender
        self.primary_phone = primary_phone

# Create a list of patient instances (more than 50 patients)
patients = [
    Patient("John", "Robert", "Doe", "Male", "123-456-7890"),
    Patient("Jane", "Marie", "Smith", "Female", "987-654-3210"),
    # ... (add more patients here)
]

def filter_patients(patients):
    filtered_patients = []

    first_name = input("Enter First Name (or press Enter to skip): ")
    middle_name = input("Enter Middle Name (or press Enter to skip): ")
    family_name = input("Enter Family Name (or press Enter to skip): ")
    gender = input("Enter Gender (or press Enter to skip): ")
    primary_phone = input("Enter Primary Phone (or press Enter to skip): ")

    for patient in patients:
        if (not first_name or patient.first_name == first_name) and \
           (not middle_name or patient.middle_name == middle_name) and \
           (not family_name or patient.family_name == family_name) and \
           (not gender or patient.gender == gender) and \
           (not primary_phone or patient.primary_phone == primary_phone):
            filtered_patients.append(patient)

    return filtered_patients

# Call the filter_patients function with the list of patient instances
filtered_patients = filter_patients(patients)

# Display filtered patients
if filtered_patients:
    print("Filtered Patients:")
    for patient in filtered_patients:
        print(f"{patient.first_name} {patient.family_name}: {patient.primary_phone}")
else:
    print("No patients match the criteria.")
