# Function to write data to report.txt
def write_student_data():
    n = int(input("Enter number of students: "))
    with open("report.txt", "w") as file:
        for _ in range(n):
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks (out of 100): "))
            entry = f"Name: {name}, Subject: {subject}, Marks: {marks}\n"
            file.write(entry)
    print("\nData successfully written to report.txt!\n")

# Function to read and analyze data from report.txt
def read_and_analyze_data():
    try:
        with open("report.txt", "r") as file:
            lines = file.readlines()
            total_students = len(lines)
            total_marks = 0

            print("--- All Student Entries ---")
            for line in lines:
                print(line.strip())
                # Extract marks from each line
                parts = line.strip().split(", ")
                for part in parts:
                    if part.startswith("Marks:"):
                        mark = int(part.split(":")[1].strip())
                        total_marks += mark

            if total_students > 0:
                avg_marks = total_marks / total_students
                print(f"\nTotal number of students: {total_students}")
                print(f"Average marks: {avg_marks:.2f}")
            else:
                print("\nNo student data found.")
    except FileNotFoundError:
        print("report.txt file not found. Please enter data first.")

# Main execution
write_student_data()
read_and_analyze_data()

