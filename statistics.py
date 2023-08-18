import json

class Patient:
    def __init__(self, first_name, middle_name, family_name, gender, primary_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.gender = gender
        self.primary_phone = primary_phone

# Create an array to store patient objects
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

# Convert patient objects to a JSON object
patients_json = [patient.__dict__ for patient in patients]

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
        if patient.gender == "Male":
            gender_statistics["Male"] += 1
        elif patient.gender == "Female":
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
