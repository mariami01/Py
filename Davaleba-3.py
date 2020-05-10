myStudentTuple = []

Numberofstudents = input("How many students are in this class? ")

while not Numberofstudents.isdigit():
    Numberofstudents = int(input("Enter only number: "))

for i in range(int(Numberofstudents)):
    myStudentIDTuple = input("Enter the Student ID (11 digit number): ")
    while not myStudentIDTuple.isdigit() and len(myStudentIDTuple) != 11:
        myStudentIDTuple = input("ID number consist of 11 digits. Enter again: ")
    myStudentTuple.append(myStudentIDTuple)

    myStudentNameTuple = input("Enter the Name of the Student: ")
    while not myStudentNameTuple.isalpha():
        myStudentNameTuple = input("Characters of the student name must be alphabet. Try again: ")
        myStudentTuple.append(myStudentNameTuple)

    myStudentLastNameTuple = input("Enter the Lastname of the Student: ")
    while not myStudentLastNameTuple.isalpha():
        myStudentLastNameTuple = input("Characters of the student Lastname must be alphabet. Try again: ")
        myStudentTuple.append(myStudentLastNameTuple)


myStudentTuple = tuple(myStudentTuple)

studentDictionary={}
for i in myStudentTuple:
    if i[0].isdigit():
        studentDictionary[i]=0


count = 1
for i in studentDictionary:
    score = input(f'Enter the score of the student {count} (score can be 0-100): ')

    while not score.isdigit():
        score = input("Score must be a digit.")
    score = int(score)
    while not 0 < score < 100:
        score = input("Score must be 0-100: ")
    studentDictionary[i] = score
    count += 1

scores = []

for i in studentDictionary:
    scores.append(studentDictionary[i])

scores = sorted(scores)
scores = scores[:10]
scores.reverse()


for i in studentDictionary:
    if studentDictionary[i] in scores:
        print(f'{i} : {scores[scores.index(studentDictionary[i])]}')

sorted_dictionary = sorted(studentDictionary.items())

for i in sorted_dictionary[0:10]:
    print(f"Score of top 10 student {i[0]} is {i[1]}")
