#Task (Find the Lowest Score of a Student)
#Given an string, perform the following actions:
#   - Use the concept of dictinory
#   - Count the number of alphabets
#   - Print the alphabets and its count

# Input Format
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

#You can attempt this for your own practice

######code below this line######


######do not change these lines, only add functionalites if needed######
if __name__ == '__main__':
    student_data = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name = input("Enter the name of the student: ")
        score = float(input("Enter the score of the student: "))
        student_data.append([name, score])