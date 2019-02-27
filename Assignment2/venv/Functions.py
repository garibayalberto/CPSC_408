from Student import Student
from sql import Sql
s = Sql()

class Functions:


    #This function validates if the student does exist in the database
    def checkStudent(self, idNumber):
        s.c.execute("SELECT StudentID from Student WHERE StudentId = ?", (int(idNumber),))
        student = s.c.fetchall()
        if student == []:
            return False
        else:
            return True

    #this function displays the board
    def displayAllStudents(self):
        s.c.execute("SELECT * FROM Student")
        total = s.c.fetchall()
        for students in total:
            print(students)
            print()
        return;

    #this function creates a new student
    def createstudent(self,fname,lname,major,gpa,fadviser):
        #creatinng a student object from the student class
        stu = Student (fname,lname,major,gpa,fadviser)
        #inserting the student's information from the object into the table
        s.c.execute("INSERT INTO Student(FirstName, LastName, Major, GPA, FacultyAdviser)"
                  "VALUES(?,?,?,?,?)",(stu.getStudentTuple()))
        s.conn.commit()

    #this function updates any student's major or adviser
    def updateStudentInfo(self,info,option):

        #this changes the major of the student
        if option == "MAJOR":
            print("Type new major:")
            newmajor = input()
            s.c.execute("UPDATE Student set Major = ? WHERE StudentID = ?",(newmajor,info))

        #this changes the adviser of the student
        elif option == "ADVISER":
            print("Type new adviser:")
            newadviser = input()
            s.c.execute("UPDATE Student set FacultyAdviser = ? WHERE StudentID = ?",(newadviser,info))

        #This changes both the major and the adviser of the student
        elif option == "BOTH":
            print("Type new major:")
            newmaj = input()
            print("Type new adviser:")
            newadvise = input()
            s.c.execute("UPDATE Student set Major = ? ,FacultyAdviser = ? WHERE StudentID = ?",(newmaj,newadvise,str(info)))

        elif option == 'q':
            return

        #this returns the student and their info to the user so they can see the changes that they made
        s.c.execute("SELECT * FROM Student WHERE StudentId = ?", (info,))
        student = s.c.fetchone()
        print(student)
        print()
        s.conn.commit()

    def searchStudents(self, option,info):
        #the while loop allows the user to continue their work without restarting if they input an invalid option
            if(option == "MAJOR"):
                s.c.execute("SELECT * FROM Student WHERE Major LIKE ?",('%' + info + '%',))
                student = s.c.fetchall()
                if student == []:
                    print("There was no major with that name")
                else:
                    for students in student:
                        print(students)
                        print()
                s.conn.commit()

            elif (option == "ADVISER"):
                s.c.execute("SELECT * FROM Student WHERE FacultyAdviser LIKE ?", ('%' + info + '%',))
                student = s.c.fetchall()
                if student == []:
                    print("There was no major with that name")
                else:
                    for students in student:
                        print(students)
                        print()
                s.conn.commit()

            elif (option == "GPA"):
                s.c.execute("SELECT * FROM Student WHERE GPA = ?", (info,))
                student = s.c.fetchall()
                if student == []:
                    print("There was no major with that name")
                else:
                    for students in student:
                        print(students)
                        print()
                s.conn.commit()

            else:
                print("What you entered was an invalid response, please try again.")
                print()


    def deleteStudent(self,idnumber):

        s.c.execute("DELETE FROM Student WHERE StudentId = ?",str(idnumber))
        print("The student has been deleted")
        print()
        s.conn.commit()