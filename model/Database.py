import json
import os
from model import Student


# Database class to handle students.data file and related functionalities
class Database:
    # Constructor to initialize attributes
    def __init__(self):
        # Get current working directory
        self.currentDir = os.getcwd()
        # Get parent directory
        self.parentDir = os.path.dirname(self.currentDir)
        # Create path for data directory where we will save students.data file
        if "CLIUniApp" not in self.parentDir:
            self.parentDir = self.currentDir
        self.dataDir = os.path.join(self.parentDir, "data")
        # Create path for students.data file
        self.dataPath = os.path.join(self.dataDir, "students.data")

    # Function to check if students.data file exists
    def isFileExists(self):
        # Check if students.data file exists
        if not os.path.exists(self.dataPath):
            # Create the Data directory if it doesn't exist
            if not os.path.exists(self.dataDir):
                os.makedirs(self.dataDir)

            # Create an empty students.data file
            with open(self.dataPath, 'w') as file:
                json.dump([], file)

    # Function to read students.data file
    def readDataFile(self):
        # Handle if students.data file does not exists
        self.isFileExists()
        # Open students.data file and read the students data as JSON
        with open(self.dataPath, 'r') as file:
            data = json.load(file)
        # Returns the data
        return data

    # Function to check if given student email and password exists in students.data
    def isEmailExist(self, studentEmail, password=None):
        # Read students.data file
        data = self.readDataFile()
        # Iterate through each student in the data
        for student in data:
            # If the current student's email matches the given email ID
            if student['email'] == studentEmail:
                # Check if password is given in the parameters
                if password:
                    # If the current student's password also matches the given password then return student
                    if student['password'] == password:
                        return student
                    else:
                        # Return None if password not matched
                        return None
                # If password is not given and email id matches, return student
                return student
        # If email id not found in data return None
        return None

    # Function to get details of the a given student ID
    def getStudentDetails(self, studentId):
        # Read students.data file
        data = self.readDataFile()
        # Iterate through each student in the data
        for student in data:
            # If the current student's ID matches the given student id then return the student
            if student['id'] == studentId:
                return student
        # If student Id not found in data return None
        return None

    # Function to write updated student details to students.data file
    def toStudentData(self, student: Student):
        # Read existing data from the file
        existingData = self.readDataFile()
        # Take given student id and convert its details to dict format
        sid = student.id
        # Flag to add new student
        flag = True
        studentData = json.loads(student.__str__())
        # Iterate through each student in the data
        for i in range(len(existingData)):
            # If the given student is already present
            if existingData[i]['id'] == sid:
                # Replace the existing record for the student with the given student details
                existingData[i] = studentData
                flag = False
                break
        # If student does not exist in file then append it to the existing data
        if flag:
            existingData.append(studentData)

        # Overwrite the updated data in the students.file
        with open(self.dataPath, 'w') as file:
            json.dump(existingData, file)

    # Function to delete a particular student from the file
    def deleteStudent(self, studentId):
        # Read existing data from the file
        existingData = self.readDataFile()
        # Index of the student we want to delete
        index = None
        # Iterate through each student in the data
        for i in range(len(existingData)):
            # If the id matches with the given student id, update the index and break the loop
            if existingData[i]['id'] == studentId:
                index = i
                break
        # If the given student is present in the file
        if index is not None:
            # Delete the student from the list
            del existingData[index]
            # Update the students.data file
            with open(self.dataPath, 'w') as file:
                json.dump(existingData, file)

    # Function to delete all students from students.data file
    def cleaStudentData(self):
        # Handle if students.data file does not exists
        self.isFileExists()
        # Rewrite the blank file
        with open(self.dataPath, 'w') as file:
            json.dump([], file)
