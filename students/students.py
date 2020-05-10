#import the information from txt file
from operator import itemgetter

mystudents = open("MyStudents.txt", "r")
myStudentTuple = tuple([i[0].strip().split('-') for i in [i.strip() .split(',') for i in mystudents.readlines()]])
print(myStudentTuple)

#create the dictionary and add grades in it

studentDictionary = {}
for i in myStudentTuple:
    studentDictionary[i[0]]=0

count=1
for i in studentDictionary:
    try:
        studentDictionary[i]=float(input(f"Enter the grade(51-100) of student{count}:"))
        if 51<studentDictionary[i]<101:
            count+=1
        else:
            print("Grade must be betwenn 51-100!")
    except ValueError:
        print("Wrong input!")

#calculate the average grade

average=0
for i in studentDictionary.values():
    average+=i
average/=len(myStudentTuple)

#calculate the median of grades

stud_median=[]
for i in sorted(studentDictionary.values()):
    stud_median.append(i)
s=len(stud_median)
stud_median.sort()
if s % 2==0:
    median1=stud_median[s//2]
    median2=stud_median[s//2 -1]
    median=(median1+median2)/2
else:
    median=stud_median[s//2]
print("Median of the students grade is: " + str(median))

#top 10 students
top_stud = []
for i in studentDictionary.values():
    top_stud=dict(sorted(studentDictionary.items(),key=itemgetter(1), reverse= True)[:10])

print("The top 10 students are " + str(top_stud))

#write top10 student information on file

top10=open("Top10Students.txt", "w")
top10.write(str("'ID': Grade \n"))
top10.write(str(top_stud))
top10.close()

#write average and median on file
grade_info=open("ExamStatistics.txt", "w")
grade_info.write("Median of the grade is ")
grade_info.write(str(median))
grade_info.write('\n')
grade_info.write("Average of the grade is ")
grade_info.write(str(average))
grade_info.close()
