"""calculate the student's grade based on the scores from the input and the predefined weights for each category"""
# define the weights for each category
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2
# get the scores from the user
midterm_exam_grade = float(input('Enter midterm exam grade 0 - 100: '))
final_exam_grade = float(input('Enter final exam grade 0 - 100: '))
assignment_one = float(input('Enter assignment 1 grade 0 - 30: '))
assignment_two = float(input('Enter assignment 2 grade 0 - 30: '))
quiz_one = float(input('Enter quiz 1 grade 0 - 20: '))
quiz_two = float(input('Enter quiz 2 grade 0 - 20: '))

is_valid = True

# test the midterm and final exam grades are within the valid range
if 0 <= midterm_exam_grade <= 100 and 0 <= final_exam_grade <= 100:
    # Exams are already on a 0-100 scale
    exam_grade = ((midterm_exam_grade + final_exam_grade) / 2) * EXAM_WEIGHT
else:
    print('invalid input for exams')
    is_valid = False

# test the assignment grades are within the valid range
if 0 <= assignment_one <= 30 and 0 <= assignment_two <= 30:
    # Convert average from 0-30 scale to percentage (0-100 scale), then multiply by weight
    assignment_avg_percentage = (((assignment_one + assignment_two) / 2) / 30) * 100
    assignment_grade = assignment_avg_percentage * ASSIGNMENT_WEIGHT
else:
    print('invalid input for assignments')
    is_valid = False

# test the quiz grades are within the valid range
if 0 <= quiz_one <= 20 and 0 <= quiz_two <= 20:
    # Convert average from 0-20 scale to percentage (0-100 scale), then multiply by weight
    quiz_avg_percentage = (((quiz_one + quiz_two) / 2) / 20) * 100
    quiz_grade = quiz_avg_percentage * QUIZ_WEIGHT
else:
    print('invalid input for quizzes')
    is_valid = False

# add the final grade if all inputs were valid
if is_valid:
    final_grade = exam_grade + assignment_grade + quiz_grade
    print(f'The final grade is: {final_grade:.2f}%')