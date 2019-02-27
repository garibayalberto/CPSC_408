class Student:

    def __init__(self, first_name, last_name, major, gpa, adviser):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
        self.adviser = adviser

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getMajor(self):
        return self.major

    def getGPA(self):
        return self.gpa

    def getAdvisor(self):
        return self.adviser

    def getStudentTuple(self):
        return (self.getFirstName(),self.getLastName(),self.getMajor(),self.getGPA(),self.getAdvisor())