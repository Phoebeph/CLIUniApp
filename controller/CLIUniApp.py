from model.Subject import Subject
from model.Student import Student
from model.Database import Database
from model.Manager import Manager


# Class to Handle CLI Menu and User Interaction between Models and Database
class CLIUniApp:
    # Constructor to initialize model objects
    def __init__(self):
        # Object to handle Database
        self.database = Database()
        # Object to handle logged in user
        self.student: Student = None
        # Object to handle Manager
        self.manager = Manager()

    # Function to login student
    def loginStudent(self):
        print("\tStudent Sign In")
        # Initialize default student
        student = Student()
        # Loop to take correct email and password format
        while True:
            # Prompt user for email and password
            email = input("\tEmail: ")
            password = input("\tPassword: ")
            # If email or password format does not qualifies display message
            if not student.verifyEmail(email) or not student.verifyPassword(password):
                print("\tIncorrect email or password format")
            else:
                print("\temail and password formats acceptable")
                break

        # Check if email id exists
        existStudent = self.database.isEmailExist(email, password)
        # If student does not exists display message and return
        if existStudent is None:
            print("\tStudent does not exists")
            return
        # If student exists then convert subjects from dict to Subject objects
        subjects = []
        for subject in existStudent['subjects']:
            subjectObj = Subject(**subject)
            subjects.append(subjectObj)
        # Update the student object with the list of Subject objects
        existStudent['subjects'] = subjects
        student.setParameters(**existStudent)
        # Update the logged in user and show Course Menu
        self.student = student
        self.subjectMenu()
        return

    # Function to register a new student
    def registerStudent(self):
        print("\tStudent Sign Up")
        # Initialize default student
        student = Student()
        # Regenerate student id if its already exists
        while self.database.getStudentDetails(student.id):
            student.generateId()
        # Loop to take correct email and password format
        while True:
            # Prompt user for email and password
            email = input("\tEmail: ")
            password = input("\tPassword: ")
            # If email or password format does not qualifies display message
            if not student.verifyEmail(email) or not student.verifyPassword(password):
                print("\tIncorrect email or password format")
            else:
                print("\temail and password formats acceptable")
                break
        # Check if email id already exists
        existStudent = self.database.isEmailExist(email)
        # If student already exists display message and return
        if existStudent:
            print("\tStudent {0} already exists".format(existStudent["name"]))
            return
        # Prompt user for name
        name = input("\tName: ")
        print("\tEnrolling Student", name)
        # Update the student object details
        student.name = name
        student.email = email
        student.password = password
        # Add the student to the database
        self.database.toStudentData(student)
        return

    # Function to display Admin menu
    def managerMenu(self):
        # Loop until user exits
        while True:
            # Prompt admin for a choice
            choice = input("\tAdmin System (c/g/p/r/s/x): ").lower()
            # Choice to clear all students data
            if choice == 'c':
                print("\tClearing students database")
                # Prompt admin for a confirmation
                confirm = input("\tAAre you sure you want to clear the database (Y)ES/(N)O: ").upper()
                # If admin confirms then reset the database
                if confirm == 'Y':
                    self.database.cleaStudentData()
                    print("\tStudents data cleared")
            # Choice to view students categorised by their average grades
            elif choice == 'g':
                self.manager.viewStudentByGrade(self.database.readDataFile())
            # Choice to view students categorised by PASS/FAIL
            elif choice == 'p':
                self.manager.viewStudentsByCategory(self.database.readDataFile())
            # Choice to delete a particular student
            elif choice == 'r':
                # Prompt admin for a student id
                sid = input("\tRemove by ID: ")
                # Delete student if it exists else show error message
                if self.database.getStudentDetails(sid):
                    print("\tRemoving Student {0} Account".format(sid))
                    self.database.deleteStudent(sid)
                else:
                    print("\tStudent {0} doesnot exists".format(sid))
            # Choice to display all student details
            elif choice == 's':
                self.manager.viewStudent(self.database.readDataFile())
            # Choice to return to previous menu
            elif choice == 'x':
                return
            # If any invalid choice is given
            else:
                print("Invalid Option. Try Again!")

    # Function to display student menu
    def studentMenu(self):
        # Loop until user exits
        while True:
            # Prompt user for a choice
            choice = input("\tStudent System (l/r/x): ").lower()
            # Choice if user wants to login
            if choice == 'l':
                self.loginStudent()
            # Choice if user wants to register
            elif choice == 'r':
                self.registerStudent()
            # Choice to return to previous menu
            elif choice == 'x':
                return
            # If any invalid choice is given
            else:
                print("Invalid Option. Try Again!")

    # Function to display Subject enrollment menu
    def subjectMenu(self):
        # Loop until user exits
        while True:
            # Prompt user for a choice
            choice = input("\t\tStudent Course Menu (c/e/r/s/x): ").lower()
            # Choice if student wants to change password
            if choice == 'c':
                self.student.changePassword()
            # Choice if student wants to enroll in a new subject
            elif choice == 'e':
                # Try-Except to handle maximum enrollment error
                try:
                    self.student.enrollSubject()
                except Exception as e:
                    print(e)
            # Choice if student wants to remove a subject
            elif choice == 'r':
                # Try-Except to handle error
                try:
                    subjectId = input("\t\tRemove Subject by ID: ")
                    self.student.removeSubject(subjectId)
                except Exception as e:
                    print(e)
            # Choice to view enrolled subjects
            elif choice == 's':
                self.student.viewSubjects()
            # Choice to return to previous menu
            elif choice == 'x':
                return
            # If any invalid choice is given
            else:
                print("Invalid Option. Try Again!")
            # Update database after each choice
            self.database.toStudentData(self.student)

    # Main menu
    def main(self):
        # Loop until user exits
        while True:
            # Prompt user for a choice
            choice = input("University System (A) dmin, (S) tudent, X : ").upper()
            # Choice for Admin Menu
            if choice == 'A':
                self.managerMenu()
            # Choice for Student Menu
            elif choice == "S":
                self.studentMenu()
            # Choice to exit program
            elif choice == "X":
                return
            # If any invalid choice is given
            else:
                print("Invalid Option. Try Again!")


# Run from here
if __name__ == "__main__":
    cli = CLIUniApp()
    cli.main()
