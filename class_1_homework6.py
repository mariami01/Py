from datetime import date
class Lecturer:
    leCount=0

    def __init__(self, name, lastname, birth, school, faculty, position, experience):
        self.name = name
        self.lastname = lastname
        self.birth = birth
        self.school = school
        self.faculty = faculty
        self.position = position
        self.experience = experience
        Lecturer.leCount +=1
    def displayCount(self):
        print("Total Lecturer %d" % Lecturer.leCount)

    def displayLecturer(self):
        today = date.today()
        retire = today.year - self.birth
        if retire >=60:
            print("Name : ", self.name,  ", Lastname: ", self.lastname)
        else:
            pass

lect1 = Lecturer("Name1", "LastName1", 1955 , "GAU", "CS", "Professor", 5)
lect2 = Lecturer("Name2", "LastName2", 1945 , "GAU", "CS", "Lecturer", 7)
lect3 = Lecturer("Name3", "LastName3", 1959 , "GAU", "CE", "Assistant", 3)
lect4 = Lecturer("Name4", "LastName4", 1996 , "GAU", "CS", "Assistant", 4)

lect1.displayLecturer()
lect2.displayLecturer()
lect3.displayLecturer()
lect4.displayLecturer()
print("Total Lecturer %d" % Lecturer.leCount)
