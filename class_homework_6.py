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
        retire = today - self.birth
        if retire >=60:
            print("Name : ", self.name,  ", Lastname: ", self.lastname, ", Age: ", retire)
        else:
            pass

lec_list = []
lec = int(input("How many Lecturers do you have? "))
for i in range(lec):
    name =input("Name of the Lecturer: ")
    lastname =input("Last name of the Lecturer: ")
    birth = input("Birthday of the Lecturer(year,month,day): ")
    school =input("Lecturer's School: ")
    faculty =input("Lecturer's Faculty: ")
    position =input("Lecturer's Position: ")
    experience =input("Lecturer's year of experience: ")
    lec_list=lec_list.append(lec[i])
    print(lec_list)
