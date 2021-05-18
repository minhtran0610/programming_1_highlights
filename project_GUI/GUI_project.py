"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tran Sy Minh, minh.s.tran@tuni.fi, student id 050359358
This program lets the teacher enter the elementary points, basic points and
project points of the student and determines his/her final grade. The program
can also print the list of students with their grades, find a student with
his/her ID or plot a histogram of the grades.
"""

from tkinter import *
NAN = float('NaN')


class UserInterface:
    def __init__(self):
        """
        Initialize the GUI
        """
        self.__window = Tk()
        self.__window.title("Programming 1")

        # Create the components
        # Create a Entry component for the ID
        self.__ID_label = Label(self.__window, text="ID:")
        self.__ID = Entry()

        # Create a Entry component for the name
        self.__name_label = Label(self.__window, text="Name:")
        self.__name = Entry()

        # Create a Entry component for the email
        self.__email_label = Label(self.__window, text="Email:")
        self.__email = Entry()

        # Create a Entry component for the basic points
        self.__basic_points_label = Label(self.__window, text="Basic points:")
        self.__basic_points = Entry()

        # Create a Entry component for the elementary points
        self.__elementary_points_label = Label(self.__window,
                                                text="Basic points:")
        self.__elementary_points = Entry()

        # Create a Entry component for the elementary points
        self.__elementary_points_label = Label(self.__window,
                                               text="Elementary points:")
        self.__elementary_points = Entry()

        # Create a Entry component for the project points
        self.__project_points_label = Label(self.__window,
                                               text="Project points:")
        self.__project_points = Entry()

        # Create an option menu component for the exam type
        self.__exam_menu_label = Label(self.__window, text="Exam type:")

        self.__exam_types = ["Elementary", "Basic", "Extended"]
        self.__exam_option = StringVar(self.__window)
        self.__exam_option.set(self.__exam_types[0])

        self.__exam_menu = OptionMenu(self.__window, self.__exam_option, *self.__exam_types)

        # Create the buttons and the place to display contents
        # Create the Enter button to confirm input
        self.__enter_button = Button(self.__window, text="Enter", command=self.enter)

        # Create the Delete button to delete the information in the data file
        self.__delete_button = Button(self.__window, text="Delete", command=self.delete)

        # Create the Find button to find a person with his/her ID
        self.__find_button = Button(self.__window, text="Find", command=self.find)
        
        # Create a Delete A Student button to delete a single entry by the student's ID
        self.__delete_a_student_button = Button(self.__window, text="Delete A Student", command=self.delete_a_student)

        # Create the Data button to print the data of all the students entered
        self.__data_button = Button(self.__window, text="Data", command=self.data)

        # Create the Plot button to print the histogram of the scores
        self.__plot_button = Button(self.__window, text="Plot", command=self.plot)

        # Create a Quit button to quit the program
        self.__quit_button = Button(self.__window, text="Quit", command=self.stop)

        # Create a place to display the content from the program
        self.__displayed_content = Label(self.__window,
                                         text="")

        # Place the components
        self.__ID_label.grid(row=0, column=0, sticky=W)
        self.__ID.grid(row=0, column=1, columnspan=7, sticky=W+E)

        self.__name_label.grid(row=1, column=0, sticky=W)
        self.__name.grid(row=1, column=1, columnspan=7, sticky=W+E)

        self.__email_label.grid(row=2, column=0, sticky=W)
        self.__email.grid(row=2, column=1, columnspan=7, sticky=W+E)

        self.__elementary_points_label.grid(row=3, column=0)
        self.__elementary_points.grid(row=3, column=1)

        self.__basic_points_label.grid(row=3, column=2)
        self.__basic_points.grid(row=3, column=3)

        self.__project_points_label.grid(row=3, column=4)
        self.__project_points.grid(row=3, column=5)
        
        self.__exam_menu_label.grid(row=3, column=6)
        self.__exam_menu.grid(row=3, column=7)

        self.__enter_button.grid(row=4, column=3, columnspan=2, sticky=W+E)

        self.__displayed_content.grid(row=5, column=1, columnspan=6, sticky=W+E)

        self.__find_button.grid(row=6, column=0, sticky=W+E)
        self.__delete_button.grid(row=6, column=1, sticky=W+E)
        self.__delete_a_student_button.grid(row=6, column=2, sticky=W+E)
        self.__data_button.grid(row=6, column=3, columnspan=2, sticky=W+E)
        self.__plot_button.grid(row=6, column=5, sticky=W+E)
        self.__quit_button.grid(row=6, column=6, columnspan=2, sticky=W+E)

    def start(self):
        """
        Start the program
        """
        self.__window.mainloop()

    def stop(self):
        """
        Stop the program
        """
        self.__window.destroy()

    def enter(self):
        """
        Let the user enter the information of the student and his/her scores.
        Print the final grade in the UI
        """
        # Get the scores from the user
        try:
            basic_point = int(self.__basic_points.get())
        except ValueError:
            basic_point = NAN

        try:
            elementary_point = int(self.__elementary_points.get())
        except ValueError:
            elementary_point = NAN

        try:
            project_point = int(self.__project_points.get())
        except ValueError:
            project_point = NAN

        # Check if a score is an integer
        if basic_point != basic_point or elementary_point != elementary_point or project_point != project_point:
            self.__displayed_content.configure(
                text="The scores must be integers.")
            # Delete the entries
            self.delete_entries()
        # Check if the ID is duplicate
        elif self.check_if_ID_exists():
            self.__displayed_content.configure(
                text="The ID is already taken.")
            # Delete the entries
            self.delete_entries()
        # Check if there are empty entries
        elif self.check_if_empty_entries():
            self.__displayed_content.configure(
                text="No empty entries are allowed")
            # Delete the entries
            self.delete_entries()
        # Getting the grades, calculating the final grade and write to the
        # data file
        else:
            # Getting the grades for the exams and project and calculate the
            # corresponding grade
            grades_list = [grade_exercises(elementary_point), grade_exercises(basic_point), grade_projects(project_point)]
            exercise_and_project_grade = min(grades_list)

            # Getting the exam scores and calculating the possible points
            exam_type = self.__exam_option.get()
            final_grades = possible_grade_exam(exam_type)

            # Calculating the overall grade and print it out in the GUI
            final_grade = calculate_final_grade(final_grades, exercise_and_project_grade)
            # If the grade equals 0, the student failed the course
            if final_grade == 0:
                final_grade = "Failed"
            self.__displayed_content.configure(
                text=f"Final grade: {final_grade}")
            
            # Open the data file and write the information
            # If opening the file fails, print the message in the GUI
            try:
                data_file = open('data.csv', mode='a')
            except OSError:
                self.__displayed_content.configure(
                    text="Open the data file failed.")
                return

            # Write the information
            ID = self.__ID.get()
            name = self.__name.get()
            email = self.__email.get()
            print(f"{ID};{name};{email};{final_grade}", file=data_file)

            # Close the file
            data_file.close()

    def check_if_ID_exists(self):
        """
        Check if an ID is already existed in the entry. This is called in the
        self.enter() method to not let the user input duplicate ID
        """
        # Get the ID
        input_ID = self.__ID.get()

        # Check if the ID already exists
        # Open the file. If failed, display a message in the GUI
        try:
            data_file = open("data.csv", mode='r')
        except OSError:
            self.__displayed_content.configure(
                text="Open the data file failed.")
            return

        for line in data_file:
            ID = line.rstrip().split(";")[0]
            if ID == input_ID:
                return True

        return False

    def check_if_empty_entries(self):
        """
        This method check if the users let any of the entries empty. No empty
        entries are allowed
        """
        # Get all the information
        name = self.__name.get()
        ID = self.__ID.get()
        email = self.__email.get()
        basic_points = self.__basic_points.get()
        elementary_points = self.__elementary_points.get()
        project_points = self.__project_points.get()

        # Check if any of the entries are empty
        if len(name) == 0 or len(ID) == 0 or len(email) == 0 or len(basic_points) == 0 or len(elementary_points) == 0 or len(project_points) == 0:
            return True
        else:
            return False

    def delete(self):
        """
        Delete the data in the file
        """
        # Create the components for the warning window
        self.__warning_window = Toplevel(self.__window)
        self.__warning_window.title("Warning")
        self.__warning_message_label = Label(self.__warning_window,
                                             text="You are about to delete all the data. Are you sure?")
        self.__yes_button = Button(self.__warning_window, text="Yes", padx=40,
                                   command=self.delete_whole_data)
        self.__no_button = Button(self.__warning_window, text="No", padx=40,
                                   command=self.__warning_window.destroy)

        # Place the components in the Warning window
        self.__warning_message_label.grid(row=0, column=0, columnspan=2)
        self.__yes_button.grid(row=1, column=0)
        self.__no_button.grid(row=1, column=1)

    def delete_whole_data(self):
        """
        This is to finish deleting the data. This is called in the yes button
        in the Warning window.
        """
        # Open the data file. If opening the file fails, print the message
        # in the GUI
        try:
            data_file = open('data.csv', mode='w+')
        except OSError:
            self.__displayed_content.configure(
                text="Open the data file failed.")
            return

        # Print the message
        self.__displayed_content.configure(text="Data deleted!")

    def delete_entries(self):
        """
        This method is used to delete the entries when the entries of the users
        are not valid
        """
        self.__ID.delete(0, END)
        self.__name.delete(0, END)
        self.__email.delete(0, END)
        self.__basic_points.delete(0, END)
        self.__elementary_points.delete(0, END)
        self.__project_points.delete(0, END)

    def find(self):
        """
        Find the information of the student using the student ID
        """
        # Create a child window for the user to enter the ID
        self.__find_window = Toplevel(self.__window)
        self.__find_window.title("Find student by ID")
        self.__find_ID_label = Label(self.__find_window, text="Enter student ID:")
        self.__find_ID = Entry(self.__find_window)
        self.__find_ID_button = Button(self.__find_window, text="Find", padx=40, command=self.ID_search)

        # Place the elements of the window
        self.__find_ID_label.pack()
        self.__find_ID.pack()
        self.__find_ID_button.pack()

    def ID_search(self):
        """
        Search for the student with the ID given in the child Find window. This
        method is called in the Find button in the child Find window method.
        """
        # Open the file. If failed, display a message in the GUI
        try:
            data_file = open("data.csv", mode='r')
        except OSError:
            self.__displayed_content.configure(
                text="Open the data file failed.")
            return

        # Create a dictionary for the students
        students_dict = create_students_dict(data_file)

        # Get the ID
        find_ID_str = self.__find_ID.get()

        # Find the student: If the ID is not in the dictionary, print out
        # an error message in the GUI
        if find_ID_str not in students_dict:
            self.__displayed_content.configure(text="ID not found.")
        # Print the result that contains name, email, and final grade
        else:
            result = f"Name: {students_dict[find_ID_str]['name']}\n" \
                     f"Email: {students_dict[find_ID_str]['email']}\n" \
                     f"Final grade: {students_dict[find_ID_str]['final grade']}"
            self.__displayed_content.configure(text=result)

        # Close the window
        self.__find_window.destroy()

    def data(self):
        """
        Show the students' data in a new window
        """
        # Create a new window
        self.__data_window = Toplevel(self.__window)
        self.__data_window.title("Students data")
        self.__ID_heading = Label(self.__data_window, text="ID", anchor=W)
        self.__name_heading = Label(self.__data_window, text="Name", anchor=W)
        self.__email_heading = Label(self.__data_window, text="Email", anchor=W)
        self.__final_grade_heading = Label(self.__data_window, text="Final grade", anchor=W)

        # Place the components of the window
        self.__ID_heading.grid(row=0, column=0)
        self.__name_heading.grid(row=0, column=1)
        self.__email_heading.grid(row=0, column=2)
        self.__final_grade_heading.grid(row=0, column=3)

        # Add the data to the child data window
        self.add_data()

    def add_data(self):
        """
        Add the students data to the new child data window. This method is
        called inside self.data()
        """
        # Open the data file. If opening the file fails, print the message
        # in the GUI
        try:
            data_file = open('data.csv', mode='r')
        except OSError:
            self.__displayed_content.configure(
                text="Open the data file failed.")
            return

        # Create a dictionary of students
        students_dict = create_students_dict(data_file)

        # Add the data to the new window
        # The starting row in the GUI
        row = 1
        for ID in students_dict.keys():
            # Getting the information
            name = students_dict[ID]['name']
            email = students_dict[ID]['email']
            final_grade_str = str(students_dict[ID]['final grade'])

            # Create label components for the information
            data_ID_label = Label(self.__data_window, text=ID, anchor=W)
            data_name_label = Label(self.__data_window, text=name, anchor=W)
            data_email_label = Label(self.__data_window, text=email, anchor=W)
            data_final_grade_str_label = Label(self.__data_window, text=final_grade_str, anchor=W)

            # Place the components in the current row
            data_ID_label.grid(row=row, column=0)
            data_name_label.grid(row=row, column=1)
            data_email_label.grid(row=row, column=2)
            data_final_grade_str_label.grid(row=row, column=3)

            # Next row
            row += 1

    def plot(self):
        """
        Create a histogram for the grades of the student in a new window
        """
        # Create a new window
        self.__plot_window = Toplevel(self.__window)
        self.__plot_window.title("Final grade histogram")

        # Create the label components corresponding to the grades in the histogram
        self.__5_label = Label(self.__plot_window, text="5:")
        self.__4_label = Label(self.__plot_window, text="4:")
        self.__3_label = Label(self.__plot_window, text="3:")
        self.__2_label = Label(self.__plot_window, text="2:")
        self.__1_label = Label(self.__plot_window, text="1:")
        self.__failed_label = Label(self.__plot_window, text="Failed:")

        # Create the label components for the bar
        self.__5_bar = Label(self.__plot_window)
        self.__4_bar = Label(self.__plot_window)
        self.__3_bar = Label(self.__plot_window)
        self.__2_bar = Label(self.__plot_window)
        self.__1_bar = Label(self.__plot_window)
        self.__failed_bar = Label(self.__plot_window)

        # Create the label components to display the number of students with
        # each final grade
        self.__5_number = Label(self.__plot_window)
        self.__4_number = Label(self.__plot_window)
        self.__3_number = Label(self.__plot_window)
        self.__2_number = Label(self.__plot_window)
        self.__1_number = Label(self.__plot_window)
        self.__failed_number = Label(self.__plot_window)
        
        # Place the components of the window
        self.__5_label.grid(row=0, column=0)
        self.__5_bar.grid(row=0, column=1)
        self.__5_number.grid(row=0, column=2)

        self.__4_label.grid(row=1, column=0)
        self.__4_bar.grid(row=1, column=1)
        self.__4_number.grid(row=1, column=2)

        self.__3_label.grid(row=2, column=0)
        self.__3_bar.grid(row=2, column=1)
        self.__3_number.grid(row=2, column=2)

        self.__2_label.grid(row=3, column=0)
        self.__2_bar.grid(row=3, column=1)
        self.__2_number.grid(row=3, column=2)

        self.__1_label.grid(row=4, column=0)
        self.__1_bar.grid(row=4, column=1)
        self.__1_number.grid(row=4, column=2)

        self.__failed_label.grid(row=5, column=0)
        self.__failed_bar.grid(row=5, column=1)
        self.__failed_number.grid(row=5, column=2)

        # Create the histogram
        self.histogram_creator()

    def histogram_creator(self):
        """
        Add the bars for the histogram to the child plot window. This method
        is called in the self.plot() method.
        """
        # Open the data file. If opening the file fails, print the message
        # in the GUI
        try:
            data_file = open('data.csv', mode='r')
        except OSError:
            self.__displayed_content.configure(
                text="Open the data file failed.")
            return

        # Create the bars for the grades with the * mark. Each * represents 1
        # student with that final grade.

        # Create the str variables for the bars
        five_bar_str = ""
        four_bar_str = ""
        three_bar_str = ""
        two_bar_str = ""
        one_bar_str = ""
        failed_bar_str = ""

        # Get the final grades from the file and create the bars
        for line in data_file:
            final_grade = line.rstrip().split(";")[-1]
            if final_grade == "Failed":
                failed_bar_str += "*"
            elif int(final_grade) == 4:
                four_bar_str += "*"
            elif int(final_grade) == 3:
                three_bar_str += "*"
            elif int(final_grade) == 2:
                two_bar_str += "*"
            elif int(final_grade) == 1:
                one_bar_str += "*"
            else:
                five_bar_str += "*"

        # Add the bars to the child plot window
        self.__5_bar.configure(text=five_bar_str)
        self.__4_bar.configure(text=four_bar_str)
        self.__3_bar.configure(text=three_bar_str)
        self.__2_bar.configure(text=two_bar_str)
        self.__1_bar.configure(text=one_bar_str)
        self.__failed_bar.configure(text=failed_bar_str)

        # Add the number of students with each final grade
        self.__5_number.configure(text=len(five_bar_str))
        self.__4_number.configure(text=len(four_bar_str))
        self.__3_number.configure(text=len(three_bar_str))
        self.__2_number.configure(text=len(two_bar_str))
        self.__1_number.configure(text=len(one_bar_str))
        self.__failed_number.configure(text=len(failed_bar_str))

    def delete_a_student(self):
        """
        Delete a single entry by the student's ID
        """
        # Create a child window for the user to enter the ID
        self.__delete_window = Toplevel(self.__window)
        self.__delete_window.title("Delete student by ID")
        self.__delete_ID_label = Label(self.__delete_window,
                                     text="Enter student ID:")
        self.__delete_ID = Entry(self.__delete_window)
        self.__delete_ID_button = Button(self.__delete_window, text="Delete",
                                       padx=40, command=self.ID_delete)

        # Place the elements of the window
        self.__delete_ID_label.pack()
        self.__delete_ID.pack()
        self.__delete_ID_button.pack()

    def ID_delete(self):
        """
        Delete the entry for the student with the ID given in the child Delete
        window. This method is called in the Delete button in the child Delete
        window.
        """
        # Open the file. If failed, display a message in the GUI
        try:
            data_file = open("data.csv", mode='r')
        except OSError:
            self.__displayed_content.configure(
                text="Open the data file failed.")
            return

        # Get the ID
        delete_ID_str = self.__delete_ID.get()

        # Create a list of lines of the file
        lines_list = []
        for line in data_file:
            lines_list.append(line)

        # Loop through the lines and find the student with the ID, then delete
        # the line. If the ID doesn't exist, print the message in the GUI
        for line in lines_list:
            ID = line.rstrip().split(";")[0]
            if ID == delete_ID_str:
                lines_list.remove(line)
                # Open the file again in write mode, then append all the
                # remaining lines in the file
                data_file = open("data.csv", mode='w')
                for new_line in lines_list:
                    print(new_line.rstrip(), file=data_file)
                self.__displayed_content.configure(text="Student deleted!")
                # Exit the child Delete by ID window
                self.__delete_window.destroy()
                return

        self.__displayed_content.configure(text="ID not found.")

        # Exit the child Delete by ID window
        self.__delete_window.destroy()


def grade_exercises(point):
    """
    Determine the grade for the exercises depending on the exercise points.

    :param point: int,
        The points earned through the exercises
    :return grade: int,
        The grade
    """
    if point < 250:
        grade = 0
    elif 250 <= point < 350:
        grade = 1
    elif 350 <= point < 450:
        grade = 2
    elif 450 <= point < 500:
        grade = 3
    elif 500 <= point < 600:
        grade = 4
    else:
        grade = 5

    return grade


def grade_projects(point):
    """
    Determine the grade of the projects depending on the project points.

    :param point: int,
        The points earned through the projects
    :return grade: int,
        The grade
    """
    if point < 150:
        grade = 0
    elif 150 <= point < 200:
        grade = 1
    elif 200 <= point < 250:
        grade = 2
    elif 250 <= point < 450:
        grade = 3
    elif 450 <= point < 600:
        grade = 4
    else:
        grade = 5

    return grade


def possible_grade_exam(exam_type):
    """
    Determine the final grades depending on the type of exam

    :param exam_type: str,
        The type of exam the student took
    :return final_grades: list,
        The final grades the student can earn
    """
    final_grades = []

    if exam_type == "Elementary":
        final_grades = [1]
    if exam_type == "Basic":
        final_grades = [2, 3]
    if exam_type == "Extended":
        final_grades = [4, 5]

    return final_grades
        

def calculate_final_grade(final_grades, exercise_and_project_grade):
    """
    Calculate the final grades depending on the grade of the exercise and
    projects and the possible final grades the student can have.
    
    :param final_grades: list,
        The final grades the student can earn
    :param exercise_and_project_grade: int,
        The grade the student earned via exercises and projects
    :return final_grade: int,
        The final grade of the student
    """
    if final_grades == [1]:
        if exercise_and_project_grade >= final_grades[0]:
            final_grade = 1
        else:
            final_grade = 0
    else:
        if exercise_and_project_grade > final_grades[1]:
            final_grade = final_grades[1]
        elif exercise_and_project_grade < final_grades[0]:
            final_grade = exercise_and_project_grade
        else:
            final_grade = exercise_and_project_grade

    return final_grade


def create_students_dict(data_file):
    """
    Create a dict of students with the data in the file

    :param data_file: str,
        The file which is opened
    :return student_dict: dict,
        The dict of students
    """
    # The dictionary to store students information
    students_dict = {}

    # Loop through the file and append the information inside the dict.
    # The dict contains the ID as the key, and the values are a dict which
    # contains the name, email and final grade of the student.
    for line in data_file:
        [ID, name, email, final_grade] = line.rstrip().split(";")
        students_dict[ID] = {
            "name": name,
            "email": email,
            "final grade": final_grade
        }

    return students_dict


def main():
    ui = UserInterface()
    ui.start()

if __name__ == "__main__":
    main()
