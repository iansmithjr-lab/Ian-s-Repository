# Personal Profile Dictionary
students = [
    {
        "Student Name": "Jordan Walker",
        "Age": 14,
        "Grade": "9th Grade",
        "Hobbies": ["Gym", "Football"],
        "School": "Westside High"
    },
    {
        "Student Name": "Autum Johnson",
        "Age": 15,
        "Grade": "Masters",
        "Hobbies": ["Art", "Gym", "Music"],
        "School": "Eastside High"
    },
    {
        "Student Name": "Semaj Williams",
        "Age": 15,
        "Grade": "Undergraduate",
        "Hobbies": ["Football", "Music"],
        "School": "Central High"
    }
]
for student in students:
    if "Football" in student["Hobbies"]:
        print(student["Student Name"])

# Display the dictionary
#print(student_profile)
