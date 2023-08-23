import json

# Create an array to store patient data as dictionaries
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

# Convert patient data (dictionaries) to a JSON object
patients_json = patients

# Write the JSON object to a file
with open("patients.json", "w") as json_file:
    json.dump(patients_json, json_file, indent=4)

def calculate_gender_statistics(patients):
    gender_statistics = {
        "Male": 0,
        "Female": 0,
        "Other": 0
    }

    for patient in patients:
        if patient["gender"] == "Male":
            gender_statistics["Male"] += 1
        elif patient["gender"] == "Female":
            gender_statistics["Female"] += 1
        else:
            gender_statistics["Other"] += 1

    return gender_statistics

# Call the calculate_gender_statistics function
gender_stats = calculate_gender_statistics(patients)

# Display gender statistics
print("Gender Statistics:")
for gender, count in gender_stats.items():
    print(f"{gender}: {count}")
