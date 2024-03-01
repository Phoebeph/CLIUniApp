import tkinter as tk
from tkinter import Label, Entry, Button, Listbox
from model.Subject import Subject
from model.Student import Student
from model.Database import Database


# Class to Handle GUI Menu and User Interaction for Students
class GUIUniApp:
    def __init__(self):
        # Root window
        self.root = tk.Tk()
        # Logged in user
        self.student: Student = None
        # Database Handler
        self.database = Database()

    # Function to handle validation and login
    def validateLogin(self, email: str, password: str):
        # Check if email or password is empty strings and show error message to user
        if email.strip() == "" or password.strip() == "":
            self.showMessage("Email or Password field empty", msgType="ERROR")
            return
        # Default student object
        student = Student()
        # If email or password format does not qualifies display message
        if not student.verifyEmail(email) or not student.verifyPassword(password):
            self.showMessage("Incorrect email or password format", msgType="ERROR")
            return

        # Check if email id exists
        existStudent = self.database.isEmailExist(email, password)
        # If student does not exists display message and return
        if existStudent is None:
            self.showMessage("Student does not exists", msgType="ERROR")
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
        self.enrollmentWindow()

    # Function to enroll student to a new subject
    def studentEnrollment(self):
        # Try-Except to handle maximum number of enrollments
        try:
            # Try to enroll a new subject
            self.student.enrollSubject()
            # Refresh window
            self.root.withdraw()
            self.enrollmentWindow()
        except Exception as e:
            # Show error message
            self.showMessage(str(e).strip(), msgType="ERROR")

    # Function to display Login Page
    def loginPage(self):
        # Close existing window
        self.root.withdraw()
        # Display window
        window = tk.Tk()
        # Configure background of the window
        window.configure(bg="teal")
        # Title of the Window
        window.title("Login")

        # Create labels and input fields for username and password
        loginLabel = Label(window, text="LOGIN WINDOW", bg="teal", fg="white")
        usernameLabel = Label(window, text="Username:", bg="teal", fg="white")
        usernameEntry = Entry(window, bg="teal")
        passwordLabel = Label(window, text="Password:", bg="teal", fg="white")
        passwordEntry = Entry(window, bg="teal")

        # Create a Login button with a custom background and foreground color
        loginButton = Button(window, text="Login", command=lambda: self.validateLogin(usernameEntry.get(), passwordEntry.get()), bg="teal", fg="black")

        # Use the grid layout manager to position widgets
        loginLabel.grid(row=0, column=0, columnspan=2)
        usernameLabel.grid(row=1, column=0)
        usernameEntry.grid(row=1, column=1)
        passwordLabel.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1)
        loginButton.grid(row=3, column=0, columnspan=2)

        # Update root window
        self.root = window
        # Start the main loop to display the window
        self.root.mainloop()

    # Function to display Message window
    def showMessage(self, message, msgType):
        # Define a dictionary for text colors based on the 'msgType'
        COLORS = {"ERROR":"red", "INFO":"blue", "SUCCESS":"green"}
        # Create a new message window
        window = tk.Tk()
        # Title of the Window
        window.title(msgType)
        # Size of the Window
        window.geometry("300x150")
        # Create a label with the custom message and text color based on 'type'
        msgLabel = Label(window, text=message, bg="white", fg=COLORS.get(msgType, "black"))
        msgLabel.pack(fill="both", expand=True)
        # Create a button to close window
        okButton = Button(window, text="OK", command=window.withdraw, bg="teal", fg="black")
        okButton.pack(fill="both", expand=True)
        # Start the main loop for the window to display the message
        window.mainloop()

    # Function to display Enrollment window
    def enrollmentWindow(self):
        # Close the current window
        self.root.destroy()
        # Create new window
        window = tk.Tk()
        # Title of the Window
        window.title("ENROLLMENT")
        # Configure background of the window
        window.configure(bg="teal")
        # Size of window
        window.geometry("300x150")
        # Create a label to display total number of subjects enrolled
        msg = "You are enrolled in {0} out of 4 subjects".format(len(self.student.subjects))
        msgLabel = Label(window, text=msg, bg="teal", fg="white")
        # Create a enrollment button
        enrollButton = Button(window, text="Enroll", command=self.studentEnrollment, bg="teal", fg="black")
        # Create a enrollment button
        subjectButton = Button(window, text="Show Enrolled Subjects", command=self.showSubjects, bg="teal", fg="black")
        # Set layout of the window
        msgLabel.pack(fill="both", expand=True)
        enrollButton.pack(fill="both", expand=True)
        subjectButton.pack(fill="both", expand=True)

        # Update root window
        self.root = window
        # Start the main loop for the window to display the message
        self.root.mainloop()

    # Function to display subjects list
    def showSubjects(self):
        # Get subject list
        subjects = self.student.subjects.copy()

        # Create a new window
        window = tk.Toplevel(self.root)
        # Title of the Window
        window.title("ENROLLED SUBJECTS")
        # Configure background of the window
        window.configure(bg="teal")
        # Size of window
        window.geometry("300x150")
        # Create a Listbox widget
        listbox = Listbox(window, bg="teal", fg="white")
        listbox.pack(fill="both", expand=True)

        # Add subjects from the list to the Listbox
        for subject in subjects:
            msg = "Subject::{0} -- mark = {1} -- grade = {2}".format(subject.subject, subject.mark, subject.grade)
            listbox.insert("end", msg)
        # Display window
        window.mainloop()


# Run from here
if __name__ == "__main__":
    gui = GUIUniApp()
    gui.loginPage()


