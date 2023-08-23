import json

class Patient:
    def __init__(self, first_name, middle_name, family_name, gender, primary_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.gender = gender
        self.primary_phone = primary_phone

patients = [
    Patient("John", "Robert", "Doe", "Male", "1234567890"),
    Patient("Jane", "Marie", "Smith", "Female", "9876543210"),
    Patient("Michael", "David", "Williams", "Male", "6565564642"),
    Patient("Emily", "Nicole", "Johnson", "Female", "65655562242"),
    Patient("Daniel", "Joseph", "Martinez", "Male", "6345621879"),
    Patient("Olivia", "Grace", "Taylor", "Female", "9871234560"),
    Patient("Christopher", "Lee", "Davis", "Male", "5655555444"),
    Patient("Ava", "Elizabeth", "Wilson", "Female", "7890123456"),
    Patient("William", "Andrew", "Rodriguez", "Male", "4567890123"),
    Patient("Sophia", "Ann", "Anderson", "Female", "9876543210"),
    Patient("Matthew", "Ryan", "Garcia", "Male", "7894561230"),
    Patient("Isabella", "Rose", "Moore", "Female", "1239874560"),
    Patient("Ethan", "James", "Lee", "Male", "2345678901"),
    Patient("Mia", "Lynn", "Thompson", "Female", "3456789012"),
    Patient("Andrew", "William", "Clark", "Male", "4567890123"),
    Patient("Charlotte", "Marie", "Turner", "Female", "5678901234"),
    Patient("Benjamin", "Michael", "White", "Male", "6789012345"),
    Patient("Lily", "Grace", "Robinson", "Female", "7890123456"),
    Patient("Samuel", "Thomas", "Davis", "Male", "8901234567"),
    Patient("Aria", "Emily", "Jackson", "Female", "9012345678")
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

# Call the filter_patients function with the array of patient objects
filtered_patients = filter_patients(patients)

# Convert filtered patient objects to a JSON object
filtered_patients_json = [patient.__dict__ for patient in filtered_patients]

# Write the JSON object to a file
with open("filtered_patients.json", "w") as json_file:
    json.dump(filtered_patients_json, json_file, indent=4)

# Display filtered patients
if filtered_patients:
    print("Filtered Patients:")
    for patient in filtered_patients:
        print(f"{patient.first_name} {patient.family_name}: {patient.primary_phone}")
else:
    print("No patients match the criteria.")

