import mysql.connector
from mysql.connector import errorcode
from dBCreate import *
import datetime

class newEx5:
    def __init__(self, cnx):
        self.cnx = cnx
    
    def validate_dob(date_text):
        try:
            datetime_birth = datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return datetime_birth
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            return None
    
    def connectdB(cursor, DB_NAME):
        try:
            cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor, DB_NAME)
                print("Database {} created successfully.".format(DB_NAME))
                self.cnx.database = DB_NAME
            else:
                print(err)
                exit(1)

    def create_database(cursor, DB_NAME):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def enroll_student(cursor, values):
        query = ("INSERT INTO students"
                "VALUES (%d, %s, %s, %s, %s, %s)")
        cursor.execute(query, values)
        self.cnx.commit()

    def register_course(cursor, values):
        query = ("INSERT INTO courses"
                "VALUES (%d, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query, values)
        self.cnx.commit()
                 
    def register_student_course(cusor, values):
        query = ("INSERT INTO course_registration"
                "VALUES (%d, %d)")
        cursor.execute(query, values)
        self.cnx.commit()
                 
    def print_course_enrollment(cursor, course_id):
        query = ("SELECT course_name"
                "FROM courses"
                "WHERE course_id = %d")
        cursor.execute(query, course_id)
        print("Enrollment List for %s".format(cursor[0]))
        
        query = ("SELECT student_id, last_name, first_name"
                 "FROM course_registration"
                 "WHERE course_id = %d")
        cursor.exeute(query, course_id)
        for (index, (student_id, last_name, first_name)) in enumerate(cursor):
            print("%d. %d  %s, %s").format(index, student_id, last_name, first_name)
    
    def print_student_study_list(cursor, student_id):
        query = ("SELECT last_name, first_name"
                "FROM students"
                "WHERE student_id = %d")
        cursor.execute(query, student_id)
        student_name = cursor[0]
        print("Study List for %s, %s".format(student_name[0], student_name[1]))
        
        query = ("SELECT department_name, course_id, course_type, course_name"
                 "FROM course_registration"
                 "WHERE student_id = %d")
        cursor.exeute(query, student_id)
        for (dept_name, course_id, course_type, course_name) in cursor:
            print("%s  %d %s : %s").format(dept_name, course_id, course_type, course_name)
            
    def print_student_daily_timetable(cursor, values):
        query = ("SELECT cr.course_id, c.department_name, c.course_type, c.course_name, c.start_time, c.end_time"
                "FROM course_registration cr JOIN courses c"
                "ON cr.course_id = c.course_id"
                "WHERE cr.student_id = %d AND c.days = %s"
                "ORDER BY c.start_time")
        cursor.execute(query, values)
        print("Course schedule on %s".format(values[1]))
        for (course_id, dept_name, course_type, course_name, start_time, end_time) in cursor:
            print("%s to %s. %s %d %s").format(start_time, end_time, dept_name, course_id, course_type)
        
    def print_table(cursor, table_name):
        query = ("SELECT *"
                "FROM %s")
        cursor.execute(query, table_name)
        for row in cursor:
            print(row)

def main():
    # code here
    cnx = mysql.connector.connect(user='root',password ='root', auth_plugin='mysql_native_password')
    dbcon = newEx5(cnx)
    cursor = cnx.cursor()
    dbcon.connectdB(cursor, DB_NAME)
    
    # get user input now
    input_string = "Please provide an option\n"
    "1. Enroll a new student"
    "2. Register a new course"
    "3. Register a student for a course"
    "4. Print all students in a course"
    "5. Print all courses for a student"
    "6. Print the time-table for a student on a given weekday"
    "7. Print courses table"
    "8. Print students table"
    "9. Print the course registrations table"
    "10. Exit the program"
    while(true):        
        choice = input(input_string)
        while (isinstance(choice, int)):
            print("Please give a valid input")
            choice = input(input_string)
        if(choice ==1):
            student_id = 'DEFAULT' # AUTO_INCREMENT
            last_name = input("Please input student's last name")
            first_name = input("Please input student's first name")
            dob = input("Please input the Student's Date of Birth as YYYY-MM-DD");
            datetime_birth = validate_dob(dob)
            while(datetime_birth is None):
                datetime_birth = validate_dob(dob)
            gender = input("Please input the student's gender M/F");
            while (gender== 'M' | gender == 'F'):
                print("please give a valid gender")
                gender = input("Please input the student's gender M/F");
            enrollment_date = datetime.today()
            values = (student_id, last_name, first_name, gender, datetime_birth, enrollment_date)
            cursor = enroll_student(cursor, values)
        elif(choice == 2):
            course_id = 'DEFAULT'
            course_name = input("Pleae enter new course name");
            dept_name = input("Please enter course department");
            days = input("Please enter days of the week e.g. Mon, Wed, Fri or Tue, Thu")
            start_time_input = input("Please enter daily course start time as HH:MM e.g. 16:30 for 4.30pm")
            start_time = datetime.strptime(start_time_input, "%H:%M")
            end_time_input = input("Please enter daily course end time as HH:MM e.g. 16:30 for 4.30pm")
            end_time = datetime.strptime(end_time_input, "%H:%M")
            course_type = input("Please enter course type: L/P/D")
            values = (course_id, course_name, days, start_time, end_time, course_type, dept_name)
            cursor = register_course(cursor, values)
        elif(choice==3):
            reg_id = 'DEFAULT'
            student_id = input("Pleae input 6 digit student ID")
            course_id = input("Please input 4 digit course ID")
            values = (reg_id, student_id, course_id)
            cursor = register_student_course(cusor, values)
        elif(choice==4):
            course_id = input("Please input 4 digit course ID")
            cursor = print_course_enrollment(cursor, course_id)
        elif(choice==5):
            student_id = input("Please input 6 digit student ID")
            cursor = print_student_study_list(cursor, student_id);
        elif(choice==6):
            student_id = input("Please input 6 digit student ID")
            day = input("Please input the 3 letter weekday e.g. Tue")
            values = (student_id, day)
            cursor = print_student_daily_timetable(cursor, values);
        elif(choice==10):
            print('Exiting.')
            break
        else:
            print("Not a supported option")



if __name__ == "__main__":
    main()