import os

# Load student data from file
def loadStudentData(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [
            {
                "id": int(data[0]),
                "name": data[1],
                "coursework": list(map(int, data[2:5])),
                "exam": int(data[5])
            }
            for data in (line.strip().split(',') for line in lines[1:])
        ]

# Calculate total and grade for a student
def calculateResults(student):
    coursework_total = sum(student["coursework"])
    overall_total = coursework_total + student["exam"]
    percentage = (overall_total / 160) * 100
    grade = 'A' if percentage >= 70 else 'B' if percentage >= 60 else 'C' if percentage >= 50 else 'D' if percentage >= 40 else 'F'
    return coursework_total, student["exam"], percentage, grade

# Display a student's record
def displayStudentRecord(student):
    coursework, exam, percent, grade = calculateResults(student)
    print(f"Name: {student['name']}, ID: {student['id']}")
    print(f"Coursework: {coursework}, Exam: {exam}, Percentage: {percent:.2f}%, Grade: {grade}\n")

# Display all student records
def viewAllRecords(students):
    total_percentage = sum(calculateResults(s)[2] for s in students)
    for student in students:
        displayStudentRecord(student)
    print(f"Total Students: {len(students)}, Average Percentage: {total_percentage / len(students):.2f}%")

# Display specific student record by name or ID
def viewIndividualRecord(students):
    query = input("Enter student name or ID: ")
    student = next((s for s in students if query.lower() == s["name"].lower() or query == str(s["id"])), None)
    if student:
        displayStudentRecord(student)
    else:
        print("Student not found.")

# Display the record of the student with the highest/lowest overall score
def showExtremeScorer(students, high=True):
    student = max(students, key=lambda s: sum(s["coursework"]) + s["exam"]) if high else min(students, key=lambda s: sum(s["coursework"]) + s["exam"])
    print(f"\n{'Highest' if high else 'Lowest'} Scoring Student:")
    displayStudentRecord(student)

# Main function to handle menu options
def studentManager():
    filename = "studentMarks.txt"
    if not os.path.exists(filename):
        print("Error: studentMarks.txt file not found.")
        return

    students = loadStudentData(filename)
    options = {
        '1': lambda: viewAllRecords(students),
        '2': lambda: viewIndividualRecord(students),
        '3': lambda: showExtremeScorer(students, high=True),
        '4': lambda: showExtremeScorer(students, high=False)
    }

    while True:
        print("\nStudent Manager Menu:\n1. View all student records\n2. View individual student record\n3. Show student with highest total score\n4. Show student with lowest total score\n5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Goodbye!")
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice. Try again.")

# Run the program
studentManager()

