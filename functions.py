import numpy as np



def calculate_total(marks):
    total = sum(marks)
    return total


def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"



def check_pass_fail(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"

    return "Pass"


def find_highest_mark(marks):
    return max(marks)


def find_lowest_mark(marks):
    return min(marks)



def calculate_numpy_average(marks):
    return np.mean(marks)

def calculate_subject_averages(marks_data):
    averages = np.mean(marks_data, axis=0)
    return averages

def find_top_performers(names, averages):
    top_students = []

    for name, average in zip(names, averages):
        if average >= 80:
            top_students.append(name)

    return top_students