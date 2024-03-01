import random
import re
from model.Subject import Subject


# Student class to handle student model and related functionalities
class Student:
    # Constructor to initialize attributes
    def __init__(self):
        # Generating random Student Id
        self.id = self.generateId()
        self.name = ''
        self.subjects = []
        self.email = ''
        self.password = ''

    # Function to update various parameter for student object
    def setParameters(self, id=None, name=None, subjects=None, email=None, password=None):
        # If a parameter is not passed in function then take existing value else given updated value
        self.id = id if id else self.id
        self.name = name if name else self.name
        self.subjects = subjects if subjects else self.subjects
        self.email = email if email else self.email
        self.password = password if password else self.password

    # Function to generate random 6 digit ID and return it
    def generateId(self):
        # Generate random int between 1 and 999999 and fill left side with 0 till len is 6
        number = str(random.randint(1, 999999))
        number = '0' * (6 - len(number)) + number
        return number

    # Function to verify if given email id follows required regex pattern
    def verifyEmail(self, email):
        emailRegex = r'^[a-zA-Z]+(\.[a-zA-Z]+)+@university\.com$'
        return re.match(emailRegex, email) is not None

    # Function to verify if given password follows required regex pattern
    def verifyPassword(self, password):
        passwordRegex = r'(^[A-Z]+)([a-zA-Z]{5,})(\d{3,}).*$'
        return re.match(passwordRegex, password) is not None

    # Function to change student password
    def changePassword(self):
        # Prompt the user to enter a new password.
        print("\t\tUpdating Password")
        newPassword = input("\t\tNew Password: ")
        # Check if the new password meets the required format using the verifyPassword method and if not return
        if not self.verifyPassword(newPassword):
            print("\t\tIncorrect email or password format")
            return
        # Prompt the user to confirm the new password
        while True:
            confirmPassword = input("\t\tConfirm Password: ")
            # Check if the confirmation matches the new password
            if newPassword != confirmPassword:
                # If the confirmation doesn't match, inform the user and loop to try again
                print("\t\tPassword does not match - try again")
            else:
                # If the confirmation matches, update the password attribute and return
                self.password = newPassword
                return

    # Function to enroll student to a new Subject
    def enrollSubject(self):
        # Check if the student is already enrolled in 4 subjects
        if len(self.subjects) == 4:
            # Raise an exception if the student is already enrolled in the maximum allowed subjects
            raise Exception("\t\tStudents are allowed to enroll in 4 subjects only")
        # Create a new subject instance
        subject = Subject()
        # Add the new subject to the student's list of enrolled subjects
        self.subjects.append(subject)
        # Display a message indicating the subject the student is enrolling in
        print("\t\tEnrolling in Subject-{0}".format(subject.subject))
        # Display the number of subjects the student is currently enrolled in
        print("\t\tYou are now enrolled in {0} out of 4 subjects".format(len(self.subjects)))

    # Function to remove the given subject from enrollment
    def removeSubject(self, subjectId):
        # Check if the student is not currently enrolled in any subjects
        if len(self.subjects) == 0:
            # Raise an exception if the student is not enrolled in any subjects
            raise Exception("\t\tNot enrolled to any subjects")

        # Iterate through the student's enrolled subjects
        for subject in self.subjects:
            # Check if the current subject matches the subjectId to be removed
            if subject.subject == subjectId:
                print("\t\tDropping Subject-{0}".format(subject.subject))
                # Remove the subject from the student's list of enrolled subjects
                self.subjects.remove(subject)
                print("\t\tYou are now enrolled in {0} out of 4 subjects".format(len(self.subjects)))
                # Return after removing the subject
                return
        # Raise an exception if the student is not enrolled in the given subject
        raise Exception("\t\tNot enrolled to the given subject")

    # Function to display the list of enrolled subjects and marks and grade
    def viewSubjects(self):
        print("\t\tShowing {0} subjects".format(len(self.subjects)))
        # Iterate through the student's enrolled subjects
        for subject in self.subjects:
            # Display Subject's name and the student's marks and grade in that subject
            print("\t\t[ Subject::{0} -- mark = {1} -- grade = {2} ]".format(subject.subject, subject.mark, subject.grade))

    # Override String function to return a custom string version of the Class
    def __str__(self) -> str:
        # Create a copy of the student object's attributes in a dictionary
        studentDict = self.__dict__.copy()
        # Initialize an empty list to store subject information
        subjectsList = []
        # Iterate through the student's enrolled subjects and add their dict version to the subjectsList
        for subject in self.subjects:
            subjectsList.append(subject.__dict__.copy())
        # Replace the 'subjects' attribute in the student dictionary with the dict version of subjects
        studentDict['subjects'] = subjectsList
        # Return the student object as a JSON-like string representation with double quotes
        return str(studentDict).replace("'", "\"")
