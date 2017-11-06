import random


def grade_generator(students):

    for student_id in range(1, students+1):
        
        random_num = random.randint(60, 100)
        if random_num >= 90:
            grade = "A"
        elif random_num >= 80:
            grade = "B"
        elif random_num >= 70:
            grade = "C"
        elif random_num >= 60:
            grade = "D"
        else: 
            grade = "F"

        grades.append({'student': student_id,'grade': random_num, 'letter_grade': grade})
        


def print_grades(grades):
    print "Student Scores and Grades"
    for i in grades:    
        print "Student: {}; Score: {}; Your grade is {}".format(i['student'], i['grade'],  i['letter_grade'])
       
    
    


grades = []
grade_generator(15)
print_grades(grades)