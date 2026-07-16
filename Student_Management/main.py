import os

def add_student():
    '''This Function Added Student Details'''

    if __name__ == "__main__":
        os.system("cls" if os.name == "nt" else "clear")
        print("-" *50)
        print("Submit The Following Details If Not have Any Use Nil")
        print("-" *50)
    
    details = ["Name","Course","P.Num"]
    student_record = []

    
    for i in details:
        user_input = input(f"Enter Student {i}: ")
        student_record.append(user_input)
        
    with open ("Student_Data.txt","a") as data:
        data.write(", ".join(student_record) + "\n")
        
    print("-"*50)
    print("Data Successfully Added In Records")

def delete_student_record():
    user_input = input("Search For Student To Delete: ").strip().lower()

    with open("Student_Data.txt", "r") as data:
        lines = data.readlines()

    found = False

    with open("Student_Data.txt", "w") as data:
        for line in lines:
            if user_input in line.lower():
                found = True
                user_confirmation = input(
                    f"Are You Sure To Delete '{line.strip()}'? (Y/N): "
                ).upper()

                if user_confirmation == "Y":
                    print("Successfully Deleted")
                    continue      

            data.write(line)      

    if not found:
        print("No Data Found :/")

def search_info():
    '''Search Student Data'''

    user_input = input("Search For Student: ").strip().lower()

    found = False

    with open("Student_Data.txt", "r") as data:
        for line in data:
            if user_input in line.lower():
                print("-"*50)
                print(line.strip())
                found = True

    if not found:
        print("No Data Found :/")
        

MENU = [

    ("Add Student",   add_student),
    ("Search Records", search_info),
    ("Delete Record", delete_student_record),
    ("Exit", None)
]

def main():

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 55)
        print("  Student Management System")
        print("=" * 55)
        for i, (label, _) in enumerate(MENU, 1):
            print(f"   {i}.  {label}")
        print("=" * 55)

        try:
            choice = int(input("\n  Enter option: ").strip())
        except (ValueError, KeyboardInterrupt):
            print("\n  Invalid input. Try again.")
            input("\n  Press Enter to continue...")
            continue

        if choice < 1 or choice > len(MENU):
            print("  Out of range.")
            input("\n  Press Enter to continue...")
            continue

        label, action = MENU[choice - 1]
        if action is None:
            print("\n  Goodbye!\n")
            break

        action()

        input("\n  Press Enter to return to menu...")

if __name__ == "__main__":
    main()