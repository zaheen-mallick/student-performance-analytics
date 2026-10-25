import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    assign_grade,
    check_pass_fail,
    find_highest_mark,
    find_lowest_mark,
    calculate_numpy_average,
    calculate_subject_averages,
    find_top_performers
)

def main():
    print("Student Performance Analytics System")

    # Loading student data
    df = pd.read_csv("students.csv")

    print("\nTotal students:", len(df))
    print("\nFirst five student records:")
    print(df.head())
    
    print("\nFirst five student records:")
    print(df.head())
    
        # Select subject columns
    subjects = ["Python", "Mathematics", "Statistics"]

    # Calculate total marks
    df["Total_Marks"] = df[subjects].apply(
        lambda row: calculate_total(row.tolist()), axis=1
    )

    # Calculate average marks
    df["Average_Marks"] = df[subjects].apply(
        lambda row: calculate_average(row.tolist()), axis=1
    )

    print("\nStudent Total and Average Marks:")
    print(df[["Name", "Total_Marks", "Average_Marks"]])
    
        # Assign grades
    df["Grade"] = df["Average_Marks"].apply(assign_grade)

    # Check pass or fail
    df["Result"] = df[subjects].apply(
        lambda row: check_pass_fail(row.tolist()), axis=1
    )

    print("\nStudent Grades and Results:")
    print(df[["Name", "Average_Marks", "Grade", "Result"]])
    
        # Find highest and lowest marks in each subject
    print("\nSubject-wise Highest and Lowest Marks:")

    for subject in subjects:
        highest = find_highest_mark(df[subject].tolist())
        lowest = find_lowest_mark(df[subject].tolist())

    print(f"{subject}: Highest = {highest}, Lowest = {lowest}")
    
    # Calculate overall class average using NumPy
    class_average = calculate_numpy_average(df["Average_Marks"].tolist())
    print("\nOverall Class Average:", round(class_average, 2))

    # Calculate subject-wise averages
    subject_averages = calculate_subject_averages(
        df[subjects].to_numpy()
    )

    print("\nSubject-wise Average Marks:")
    for subject, average in zip(subjects, subject_averages):
        print(f"{subject}: {average:.2f}")

    # Identify top performers
    top_performers = find_top_performers(
        df["Name"].tolist(),
        df["Average_Marks"].tolist()
    )

    print("\nTop Performers (Average >= 80):")
    for name in top_performers:
        print(name)

    # Display pass/fail summary
    print("\nPass/Fail Summary:")
    print(df["Result"].value_counts())

    # Display attendance analysis
    print("\nAverage Attendance:", round(df["Attendance"].mean(), 2), "%")
    low_attendance = df[df["Attendance"] < 75]
    print("Students with attendance below 75%:", len(low_attendance))

    # Save final results to CSV
    df.to_csv("student_results.csv", index=False)
    print("\nFinal results saved to student_results.csv")

    # Display final report
    print("\nFinal Student Report:")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()