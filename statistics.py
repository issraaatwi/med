class Patient:
    def __init__(self, first_name, middle_name, family_name, gender, primary_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.gender = gender
        self.primary_phone = primary_phone

# Create an array of patient objects
patients = [
    Patient("John", "Robert", "Doe", "Male", "123-456-7890"),
    Patient("Jane", "Marie", "Smith", "Female", "987-654-3210"),
    Patient("Michael", "David", "Williams", "Male", "656-556-4642"),
    Patient("Emily", "Nicole", "Johnson", "Female", "656-555-62242"),
    Patient("Daniel", "Joseph", "Martinez", "Male", "634-562-1879"),
    Patient("Olivia", "Grace", "Taylor", "Female", "987-123-4560"),
    Patient("Christopher", "Lee", "Davis", "Male", "565-555-5444"),
    Patient("Ava", "Elizabeth", "Wilson", "Female", "789-012-3456"),
    Patient("William", "Andrew", "Rodriguez", "Male", "456-789-0123"),
    Patient("Sophia", "Ann", "Anderson", "Female", "987-654-3210"),
    Patient("Matthew", "Ryan", "Garcia", "Male", "789-456-1230"),
    Patient("Isabella", "Rose", "Moore", "Female", "123-987-4560"),
    Patient("Ethan", "James", "Lee", "Male", "234-567-8901"),
    Patient("Mia", "Lynn", "Thompson", "Female", "345-678-9012"),
    Patient("Andrew", "William", "Clark", "Male", "456-789-0123"),
    Patient("Charlotte", "Marie", "Turner", "Female", "567-890-1234"),
    Patient("Benjamin", "Michael", "White", "Male", "678-901-2345"),
    Patient("Lily", "Grace", "Robinson", "Female", "789-012-3456"),
    Patient("Samuel", "Thomas", "Davis", "Male", "890-123-4567"),
    Patient("Aria", "Emily", "Jackson", "Female", "901-234-5678"),
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
