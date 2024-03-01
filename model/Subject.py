import random


# Subject class to handle subject model and related functionalities
class Subject:
    # Constructor to initialize attributes
    def __init__(self, subject=None, mark=None, grade=None):
        # Initialize the 'subject' attribute with the provided subject, or generate a new ID if not provided
        self.subject = subject if subject else self.generateId()
        # Initialize the 'mark' attribute with the provided mark, or generate a mark if not provided
        self.mark = mark if mark else self.generateMarks()
        # Initialize the 'grade' attribute with the provided grade, or generate a grade if not provided
        self.grade = grade if grade else self.generateGrade()

    # Function to generate random 3 digit ID and return it
    def generateId(self):
        # Generate random int between 1 and 999 and fill left side with 0 till len is 3
        number = str(random.randint(1, 999))
        number = '0'*(3 - len(number)) + number
        return number

    # Function to generate random marks between 25 and 100 and return it
    def generateMarks(self):
        return random.randint(25, 100)

    # Function to generate grade on the basis of the marks obtained in the subject and return it
    def generateGrade(self):
        marks = self.mark
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


