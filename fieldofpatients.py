import json

# Create an array to store patient data as dictionaries
patients = [
    {
        "first_name": "John",
        "middle_name": "Robert",
        "family_name": "Doe",
        "gender": "Male",
        "primary_phone": "1234567890",
        "group": "Group A"
    },
    {
        "first_name": "Jane",
        "middle_name": "Marie",
        "family_name": "Smith",
        "gender": "Female",
        "primary_phone": "9876543210",
        "group": "Group B"
    },
    {
        "first_name": "Michael",
        "middle_name": "David",
        "family_name": "Williams",
        "gender": "Male",
        "primary_phone": "6565564642",
        "group": "Group B"
    },
    {
        "first_name": "Emily",
        "middle_name": "Nicole",
        "family_name": "Johnson",
        "gender": "Female",
        "primary_phone": "65655562242",
        "group": "Group A"
    },
    {
        "first_name": "Daniel",
        "middle_name": "Joseph",
        "family_name": "Martinez",
        "gender": "Male",
        "primary_phone": "6345621879",
        "group": "Group B"
    },
    {
        "first_name": "Olivia",
        "middle_name": "Grace",
        "family_name": "Taylor",
        "gender": "Female",
        "primary_phone": "9871234560",
        "group": "Group A"
    },
    {
        "first_name": "Christopher",
        "middle_name": "Lee",
        "family_name": "Davis",
        "gender": "Male",
        "primary_phone": "5655555444",
        "group": "Group B"
    },
    {
        "first_name": "Ava",
        "middle_name": "Elizabeth",
        "family_name": "Wilson",
        "gender": "Female",
        "primary_phone": "7890123456",
        "group": "Group B"
    },
    {
        "first_name": "William",
        "middle_name": "Andrew",
        "family_name": "Rodriguez",
        "gender": "Male",
        "primary_phone": "4567890123",
        "group": "Group A"
    },
    {
        "first_name": "Sophia",
        "middle_name": "Ann",
        "family_name": "Anderson",
        "gender": "Female",
        "primary_phone": "9876543210",
        "group": "Group C"
    },
    {
        "first_name": "Matthew",
        "middle_name": "Ryan",
        "family_name": "Garcia",
        "gender": "Male",
        "primary_phone": "7894561230",
        "group": "Group C"
    },
    {
        "first_name": "Isabella",
        "middle_name": "Rose",
        "family_name": "Moore",
        "gender": "Female",
        "primary_phone": "1239874560",
        "group": "Group D"
    },
    {
        "first_name": "Ethan",
        "middle_name": "James",
        "family_name": "Lee",
        "gender": "Male",
        "primary_phone": "2345678901",
        "group": "Group E"
    },
    {
        "first_name": "Mia",
        "middle_name": "Lynn",
        "family_name": "Thompson",
        "gender": "Female",
        "primary_phone": "3456789012",
        "group": "Group F"
    },
    {
        "first_name": "Andrew",
        "middle_name": "William",
        "family_name": "Clark",
        "gender": "Male",
        "primary_phone": "4567890123",
        "group": "Group F"
    },
    {
        "first_name": "Charlotte",
        "middle_name": "Marie",
        "family_name": "Turner",
        "gender": "Female",
        "primary_phone": "5678901234",
        "group": "Group E"
    },
    {
        "first_name": "Benjamin",
        "middle_name": "Michael",
        "family_name": "White",
        "gender": "Male",
        "primary_phone": "6789012345",
        "group": "Group B"
    },
    {
        "first_name": "Lily",
        "middle_name": "Grace",
        "family_name": "Robinson",
        "gender": "Female",
        "primary_phone": "7890123456",
        "group": "Group A"
    },
    {
        "first_name": "Samuel",
        "middle_name": "Thomas",
        "family_name": "Davis",
        "gender": "Male",
        "primary_phone": "8901234567",
        "group": "Group B"
    },
    {
        "first_name": "Aria",
        "middle_name": "Emily",
        "family_name": "Jackson",
        "gender": "Female",
        "primary_phone": "9012345694",
        "group": "Group E"
    }
]

# Convert patient data (dictionaries) to a JSON object
patients_json = patients

# Write the JSON object to a file
with open("patients.json", "w") as json_file:
    json.dump(patients_json, json_file, indent=4)

def filter_patients_by_group(patients, search_group):
    filtered_patients = []

    for patient in patients:
        if patient.get("group") == search_group:
            filtered_patients.append(patient)

    return filtered_patients

# Prompt user to search for a specific group
search_group = input("Enter the group name to search for: ")

# Call the filter_patients_by_group function
group_patients = filter_patients_by_group(patients, search_group)

# Display patients in the searched group
if group_patients:
    print(f"Patients in the '{search_group}' group:")
    for patient in group_patients:
        print(f"{patient['first_name']} {patient['family_name']}: {patient['primary_phone']}")
else:
    print(f"No patients found in the '{search_group}' group.")
