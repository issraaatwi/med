class Patient:
    def __init__(self, first_name, middle_name, family_name, gender, primary_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.gender = gender
        self.primary_phone = primary_phone

# Create a list of patient instances
patients = [
    Patient("John", "Robert", "Doe", "Male", "123-456-7890"),
    Patient("Jane", "Marie", "Smith", "Female", "987-654-3210"),
    # ... (add more patients here)
]

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
