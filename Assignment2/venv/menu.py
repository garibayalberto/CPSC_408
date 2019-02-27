from Functions import Functions

fun = Functions()

class menu:
    #this function displays a menu to the user
    def displayMenu(self):
        print("Welcome to the student database")
        print("What would you like to do?")
        print()

        #this while statement allows the user to continue looking at the menu if they enter an invalid response
        while True:
            print("Main Menu")
            print()
            print("(1) Display all students")
            print("(2) Create a Student")
            print("(3) Update a Student's major or adviser")
            print("(4) Delete a Student")
            print("(5) Search for a Student")
            print("(6) Quit")
            print()

            option = input()

            if(option == '1'):
                print("Displaying all Students:")
                print("Student ID |  First Name | Last Name  | GPA  |  Major  | Faculty Adviser")
                print()
                fun.displayAllStudents()

            elif(option == '2'):
                print("Create New Student Menu:")

                print("Enter first name:")
                fname = input();

                print("Enter last name:")
                lname = input();

                print("Enter GPA:")
                # this is to catch if the user enters an invalid response that is not a number
                while True:
                    try:
                        gpa = float(input())
                        break
                    except ValueError:
                        print("What you entered didn't seem to be a number")
                        print("Please enter the GPA again")

                print("Enter Major:")
                major = input();

                print("Enter faculty adviser:")
                fadviser = input();

                fun.createstudent(fname, lname, major, gpa, fadviser)

                print("Student successfully added")
                print()

            elif (option == '3'):
                print("Update Student Info Menu:")

                while True:
                    print("Enter the ID of the student you would like to update:")
                    inputCheck= True

                    while inputCheck:
                        try:
                            info = int(input())
                            inputCheck = False
                        except NameError:
                            print("You did not put in a number")

                    if inputCheck == False:
                        if fun.checkStudent(info) == False:
                            print("Student does not exist")
                        else:
                            break

                # This determines if the user would like to change major or adviser both
                while True:
                    print("What would you like to update?: 'Major or 'Adviser or 'Both':")
                    choice = input().upper()
                    if(choice == "MAJOR"  or choice == "ADVISER" or choice == "BOTH"):
                        break
                    else:
                        print("what you entered was an invalid option, please try again.")
                        print()

                fun.updateStudentInfo(info,choice)

            elif (option == '4'):
                print("Delete Student Menu:")

                while True:
                    print("Enter the id of the student you would like to delete")
                    inputCheck = True

                    while inputCheck:
                        try:
                            idnumber = int(input())
                            inputCheck = False
                        except NameError:
                            print("You did not put in a number")

                    if inputCheck == False:
                        if fun.checkStudent(idnumber) == False:
                            print("Student does not exist")
                        else:
                            break

                fun.deleteStudent(idnumber)

            elif (option == '5'):
                print("How would you like to search by 'Major' , 'GPA' , 'Adviser':")
                choice = input().upper()
                print("What is the value you are searching for, example: 3.0 , Rene, Comp Sci:")
                info =  input()

                fun.searchStudents(choice, info)

            elif (option == '6'):
                print("Thank you for using our system. Goodbye :)")
                break
            #this makes sure that the user enters a valid input
            else:
                print("What you entered was not a valid option. Please enter a number 1 through 6")


