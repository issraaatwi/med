import json

class Patient:
    def __init__(self, first_name, middle_name, family_name, gender, primary_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.gender = gender
        self.primary_phone = primary_phone

# Create an array of patient objects
patients = [
    {
        "first_name": "John",
        "middle_name": "Robert",
        "family_name": "Doe",
        "gender": "Male",
        "primary_phone": "1234567890"
    },
    {
        "first_name": "Jane",
        "middle_name": "Marie",
        "family_name": "Smith",
        "gender": "Female",
        "primary_phone": "9876543210"
    },
    {
        "first_name": "Michael",
        "middle_name": "David",
        "family_name": "Williams",
        "gender": "Male",
        "primary_phone": "6565564642"
    },
    {
        "first_name": "Emily",
        "middle_name": "Nicole",
        "family_name": "Johnson",
        "gender": "Female",
        "primary_phone": "65655562242"
    },
    {
        "first_name": "Daniel",
        "middle_name": "Joseph",
        "family_name": "Martinez",
        "gender": "Male",
        "primary_phone": "6345621879"
    },
    {
        "first_name": "Olivia",
        "middle_name": "Grace",
        "family_name": "Taylor",
        "gender": "Female",
        "primary_phone": "9871234560"
    },
    {
        "first_name": "Christopher",
        "middle_name": "Lee",
        "family_name": "Davis",
        "gender": "Male",
        "primary_phone": "5655555444"
    },
    {
        "first_name": "Ava",
        "middle_name": "Elizabeth",
        "family_name": "Wilson",
        "gender": "Female",
        "primary_phone": "7890123456"
    },
    {
        "first_name": "William",
        "middle_name": "Andrew",
        "family_name": "Rodriguez",
        "gender": "Male",
        "primary_phone": "4567890123"
    },
    {
        "first_name": "Sophia",
        "middle_name": "Ann",
        "family_name": "Anderson",
        "gender": "Female",
        "primary_phone": "9876543210"
    },
    {
        "first_name": "Matthew",
        "middle_name": "Ryan",
        "family_name": "Garcia",
        "gender": "Male",
        "primary_phone": "7894561230"
    },
    {
        "first_name": "Isabella",
        "middle_name": "Rose",
        "family_name": "Moore",
        "gender": "Female",
        "primary_phone": "1239874560"
    },
    {
        "first_name": "Ethan",
        "middle_name": "James",
        "family_name": "Lee",
        "gender": "Male",
        "primary_phone": "2345678901"
    },
    {
        "first_name": "Mia",
        "middle_name": "Lynn",
        "family_name": "Thompson",
        "gender": "Female",
        "primary_phone": "3456789012"
    },
    {
        "first_name": "Andrew",
        "middle_name": "William",
        "family_name": "Clark",
        "gender": "Male",
        "primary_phone": "4567890123"
    },
    {
        "first_name": "Charlotte",
        "middle_name": "Marie",
        "family_name": "Turner",
        "gender": "Female",
        "primary_phone": "5678901234"
    },
    {
        "first_name": "Benjamin",
        "middle_name": "Michael",
        "family_name": "White",
        "gender": "Male",
        "primary_phone": "6789012345"
    },
    {
        "first_name": "Lily",
        "middle_name": "Grace",
        "family_name": "Robinson",
        "gender": "Female",
        "primary_phone": "7890123456"
    },
    {
        "first_name": "Samuel",
        "middle_name": "Thomas",
        "family_name": "Davis",
        "gender": "Male",
        "primary_phone": "8901234567"
    },
    {
        "first_name": "Aria",
        "middle_name": "Emily",
        "family_name": "Jackson",
        "gender": "Female",
        "primary_phone": "9012345678"
    }
]

def filter_patients(patients):
    filtered_patients = []

    first_name = input("Enter First Name (or press Enter to skip): ")
    middle_name = input("Enter Middle Name (or press Enter to skip): ")
    family_name = input("Enter Family Name (or press Enter to skip): ")
    gender = input("Enter Gender (or press Enter to skip): ")
    primary_phone = input("Enter Primary Phone (or press Enter to skip): ")

    for patient in patients:
        if (not first_name or patient["first_name"] == first_name) and \
           (not middle_name or patient["middle_name"] == middle_name) and \
           (not family_name or patient["family_name"] == family_name) and \
           (not gender or patient["gender"] == gender) and \
           (not primary_phone or patient["primary_phone"] == primary_phone):
            filtered_patients.append(patient)

    return filtered_patients

# Call the filter_patients function with the array of patient objects
filtered_patients = filter_patients(patients)

# Write the filtered patient data to a JSON file
with open("filtered_patients.json", "w") as json_file:
    json.dump(filtered_patients, json_file, indent=4)

# Display filtered patients
if filtered_patients:
    print("Filtered Patients:")
    for patient in filtered_patients:
        print(f"{patient['first_name']} {patient['family_name']}: {patient['primary_phone']}")
else:
    print("No patients match the criteria.")


