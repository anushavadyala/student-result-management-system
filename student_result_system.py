# ============================================
#   STUDENT RESULT MANAGEMENT SYSTEM
#   Built for: Anusha Vadyala | TKR College
# ============================================

import os

# Store all students data here
students = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_line():
    print("=" * 50)

def add_student():
    print_line()
    print("       ADD NEW STUDENT")
    print_line()
    roll = input("Enter Roll Number : ").strip()
    if roll in students:
        print("❌ Student already exists!")
        return
    name = input("Enter Student Name  : ").strip()
    print("\nEnter marks out of 100:")
    subjects = ["Python", "Java", "Maths", "English", "DBMS"]
    marks = {}
    for sub in subjects:
        while True:
            try:
                m = int(input(f"  {sub} marks : "))
                if 0 <= m <= 100:
                    marks[sub] = m
                    break
                else:
                    print("  Please enter marks between 0 and 100")
            except ValueError:
                print("  Please enter a valid number")

    students[roll] = {"name": name, "marks": marks}
    print(f"\n✅ Student '{name}' added successfully!")

def calculate_result(marks):
    total = sum(marks.values())
    percentage = total / len(marks)
    if percentage >= 75:
        grade = "A"
        result = "PASS ✅"
    elif percentage >= 60:
        grade = "B"
        result = "PASS ✅"
    elif percentage >= 50:
        grade = "C"
        result = "PASS ✅"
    elif percentage >= 35:
        grade = "D"
        result = "PASS ✅"
    else:
        grade = "F"
        result = "FAIL ❌"
    return total, percentage, grade, result

def view_result():
    print_line()
    print("        VIEW STUDENT RESULT")
    print_line()
    if not students:
        print("❌ No students found!")
        return
    roll = input("Enter Roll Number : ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    s = students[roll]
    marks = s["marks"]
    total, percentage, grade, result = calculate_result(marks)

    print_line()
    print(f"  Name       : {s['name']}")
    print(f"  Roll No    : {roll}")
    print_line()
    print(f"  {'Subject':<12} {'Marks':>6}  {'Status'}")
    print_line()
    for sub, m in marks.items():
        status = "Pass" if m >= 35 else "Fail"
        print(f"  {sub:<12} {m:>6}   {status}")
    print_line()
    print(f"  Total      : {total} / {len(marks)*100}")
    print(f"  Percentage : {percentage:.2f}%")
    print(f"  Grade      : {grade}")
    print(f"  Result     : {result}")
    print_line()

def view_all_students():
    print_line()
    print("       ALL STUDENTS LIST")
    print_line()
    if not students:
        print("❌ No students added yet!")
        return
    print(f"  {'Roll':<8} {'Name':<20} {'%':>6}  {'Grade'}  {'Result'}")
    print_line()
    for roll, s in students.items():
        total, percentage, grade, result = calculate_result(s["marks"])
        r = "PASS" if "PASS" in result else "FAIL"
        print(f"  {roll:<8} {s['name']:<20} {percentage:>5.1f}%   {grade}     {r}")
    print_line()

def update_marks():
    print_line()
    print("        UPDATE STUDENT MARKS")
    print_line()
    if not students:
        print("❌ No students found!")
        return
    roll = input("Enter Roll Number : ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return
    s = students[roll]
    print(f"\nUpdating marks for: {s['name']}")
    for sub in s["marks"]:
        while True:
            try:
                m = int(input(f"  New {sub} marks : "))
                if 0 <= m <= 100:
                    s["marks"][sub] = m
                    break
                else:
                    print("  Enter marks between 0 and 100")
            except ValueError:
                print("  Enter a valid number")
    print(f"\n✅ Marks updated for '{s['name']}'!")

def delete_student():
    print_line()
    print("        DELETE STUDENT")
    print_line()
    roll = input("Enter Roll Number : ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return
    name = students[roll]["name"]
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no) : ")
    if confirm.lower() == "yes":
        del students[roll]
        print(f"✅ Student '{name}' deleted successfully!")
    else:
        print("Cancelled.")

def top_students():
    print_line()
    print("        TOP 3 STUDENTS")
    print_line()
    if not students:
        print("❌ No students found!")
        return
    ranked = []
    for roll, s in students.items():
        total, percentage, grade, result = calculate_result(s["marks"])
        ranked.append((s["name"], roll, percentage, grade))
    ranked.sort(key=lambda x: x[2], reverse=True)
    print(f"  {'Rank':<6} {'Name':<20} {'%':>6}  {'Grade'}")
    print_line()
    for i, (name, roll, pct, grade) in enumerate(ranked[:3], 1):
        medal = ["🥇","🥈","🥉"][i-1]
        print(f"  {medal} #{i:<4} {name:<20} {pct:>5.1f}%   {grade}")
    print_line()

def main():
    while True:
        print_line()
        print("  STUDENT RESULT MANAGEMENT SYSTEM")
        print_line()
        print("  1. Add New Student")
        print("  2. View Student Result")
        print("  3. View All Students")
        print("  4. Update Student Marks")
        print("  5. Delete Student")
        print("  6. View Top 3 Students")
        print("  7. Exit")
        print_line()
        choice = input("  Enter your choice (1-7) : ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_result()
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            top_students()
        elif choice == "7":
            print("\n👋 Thank you! Goodbye Anusha!\n")
            break
        else:
            print("❌ Invalid choice! Please enter 1-7")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
