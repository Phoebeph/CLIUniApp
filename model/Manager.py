# Manager class to handle manager model and related functionalities
class Manager:
    # Constructor to initialize attributes
    def __init__(self):
        self.name = 'admin'

    # Function to view students in the given data
    def viewStudent(self, data):
        print('\tStudent List')
        # Check if the 'data' list is empty
        if len(data) == 0:
            print("\t\t<Nothing to Display>")
        # Iterate through the 'data' list and display student information
        for student in data:
            print("\t{0} :: {1} --> Email: {2}".format(student["name"], student["id"], student["email"]))

    # Function to get average marks in the given list of subjects
    def getAverage(self, subjects):
        # Initialize total to 0
        total = 0
        # If no subjects enrolled
        if len(subjects) == 0:
            return 0
        # Iterate through each subjects and the marks obtained in it to the total
        for subject in subjects:
            total += int(subject["mark"])
        # Return calculated average rounded up to 2 decimal places
        return round(total / len(subjects), 2)

    # Function to generate grade on the basis of the marks and return it
    def getGrade(self, marks):
        if marks >= 85:
            grade = 'HD'
        elif marks >= 75:
            grade = 'D'
        elif marks >= 65:
            grade = 'C'
        elif marks >= 50:
            grade = 'P'
        else:
            grade = 'Z'
        return grade

    # Function to view students given in data categorised by the Grade
    def viewStudentByGrade(self, data):
        # Check if data is empty
        if len(data) == 0:
            print("\t\t<Nothing to Display>")
            return
        # Create an empty dictionary to store student information grouped by grades
        grades = {}
        # Iterate through the data to calculate average and categorize student information by grades
        for student in data:
            subjects = student["subjects"]
            avg = self.getAverage(subjects)
            grade = self.getGrade(avg)
            # Add formatted student information to the grades dictionary under the corresponding grade
            grades[grade] = grades.get(grade, []) + ["{0} :: {1} --> GRADE: {2} - MARK: {3}".format(student["name"], student['id'], grade, avg)]

        # Display student information grouped by grades
        for grade in grades.keys():
            print("\t{0} --> {1}".format(grade, grades[grade]).replace("'", ""))

    # Function to view students given in data categorised by the PASS/FAIL
    def viewStudentsByCategory(self, data):
        # Check if data is empty
        if len(data) == 0:
            print("\t\t<Nothing to Display>")
            return
        # Create an empty dictionary to store student information grouped by PASS/FAIL
        category = {"PASS": [], "FAIL": []}
        # Iterate through the data to calculate average and categorize student information by grades
        for student in data:
            subjects = student["subjects"]
            avg = self.getAverage(subjects)
            grade = self.getGrade(avg)
            # If grade is 'Z' then student has FAIL else PASS
            if grade == 'Z':
                flag = "FAIL"
            else:
                flag = "PASS"
            # Add formatted student information to the category dictionary under the corresponding PASS/FAIL
            category[flag] += ["{0} :: {1} --> GRADE: {2} - MARK: {3}".format(student["name"], student['id'], grade, avg)]

        # Display student information grouped by PASS/FAIL
        for flag in category.keys():
            print("\t{0} --> {1}".format(flag, category[flag]).replace("'", ""))

