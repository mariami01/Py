try:

    student_1 = {}
    student_2 = {}

    name_1 = input("Student Name: ")
    subjects_1 = set()
    subject_num1 = int(input("Number of subjects: "))
    for i in range(subject_num1):
        subject = input("Enter Subject: ")
        subjects_1.add(subject)
    set1 = set(subjects_1)


    name_2 = input("Student Name: ")
    subjects_2 = set()
    subject_num2 = int(input("Number of subjects: "))
    for i in range(subject_num2):
        subject = input("Enter Subject: ")
        subjects_2.add(subject)

    set1 = set(subjects_1)
    set2 = set(subjects_2)

    student_1.update({name_1: subjects_1})
    student_2.update({name_1: subjects_2})



except:
    print("Something went wrong")

print("intersection : ", set1 & set2)
print("Union : ", set1 | set2)
print("Symmetric Difference : ", set1 ^ set2)
print("Difference set1 - set2 : ", set1 - set2)
print("Difference set2 - set1", set2 - set1)
print("Subset", set1 <= set2)
print("Superset", set1 >= set2)
