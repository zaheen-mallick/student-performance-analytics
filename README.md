# Student Performance Analytics System

## Project Objective

The Student Performance Analytics System is a Python-based project designed to analyze student academic performance using marks and attendance data. It calculates total marks, average marks, grades, pass/fail results, and class performance statistics.

## Technologies Used

- **Python** — program logic, loops, and reusable functions
- **Pandas** — loading and analyzing student data using DataFrames
- **NumPy** — numerical calculations and average marks
- **CSV** — storing student records and analysis results

## Dataset

The project uses a CSV dataset containing 20 student records with the following fields:

- Student ID
- Name
- Department
- Python marks
- Mathematics marks
- Statistics marks
- Attendance percentage

## Implementation

The project is implemented using Python functions, Pandas DataFrames, and NumPy calculations.

1. Loads student records from `students.csv` using Pandas.
2. Calculates total and average marks for each student.
3. Assigns grades based on average marks.
4. Determines pass or fail based on subject marks.
5. Identifies the highest and lowest marks in each subject.
6. Calculates the overall class average.
7. Analyzes average marks for each subject.
8. Identifies top-performing students with an average of 80 or above.
9. Analyzes student attendance.
10. Saves the processed results to `student_results.csv`.

## Key Features

- Student dataset management using CSV files
- Automated total and average mark calculations
- Grade assignment and pass/fail classification
- Subject-wise performance analysis
- Identification of top-performing students
- Class performance summary
- Attendance analysis
- Export of final results to a CSV file

## Results and Output

The program successfully processes 20 student records and generates individual performance results.

The analysis includes:

- Total and average marks for each student
- Grades and pass/fail results
- Highest and lowest marks in each subject
- Overall class average
- Subject-wise average marks
- Top-performing students
- Attendance statistics

### Sample Analysis Results

| Metric | Result |
|---|---:|
| Total students | 20 |
| Overall class average | 71.58 |
| Highest student average | 93.67 |
| Lowest student average | 37.67 |
| Average attendance | 83.50% |

### Subject-wise Average Marks

| Subject | Average |
|---|---:|
| Python | 70.85 |
| Mathematics | 71.20 |
| Statistics | 72.70 |

### Output Files

- `students.csv` — original student dataset
- `student_results.csv` — processed dataset containing total marks, average marks, grades, and pass/fail results

## Final Outcome

The project demonstrates how Python, Pandas, and NumPy can be used to automate student performance calculations and summarize academic and attendance data.

## Challenges and Learning

During this project, I practised:

- Reading and processing CSV data using Pandas.
- Working with DataFrames and selecting specific columns.
- Creating reusable Python functions.
- Using loops and conditional statements for decision-making.
- Applying NumPy for numerical calculations.
- Calculating subject-wise and overall performance statistics.
- Exporting processed data to a CSV file.
- Organizing a Python project into separate files.

This project helped me strengthen my understanding of Python programming and basic data analysis.

## Project Structure

```text
student-performance-analytics/
├── students.csv
├── student_results.csv
├── functions.py
├── main.py
└── README.md
```

## GitHub Repository

[GitHub_repository_Link](https://github.com/zaheen-mallick/student-performance-analytics).