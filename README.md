# Exam Grading System

This repository contains an **Exam Grading System** built with two primary components:

1. **Streamlit App** - A web interface for students to take the exam.
2. **Grading Python Script** - A Python script to grade the students' answers based on pre-defined solutions.

## Table of Contents
- [Overview](#overview)
- [Streamlit App](#streamlit-app)
- [Grading Python Script](#grading-python-script)
- [Running the Application](#running-the-application)
- [License](#license)

## Overview

This system allows students to take an exam through a Streamlit-based web application. After submitting their answers, the `grading.py` script automatically grades the students' responses based on pre-defined correct solutions. The grading includes both multiple-choice questions and open-ended questions, where open-ended answers are graded using text similarity metrics.

## Streamlit App

The Streamlit app serves as the user interface for the exam. Below are the steps involved in using the app:

### Features:
- **Student Validation**: The student inputs their matriculation number and name. The app checks if these details match the allowed students list.
- **Student Information**: After validation, students provide their name and matriculation number to start the exam.
- **Exam Questions**: The exam includes multiple-choice questions, true/false questions, and open-ended questions.
- **Answer Submission**: Students can submit their answers, which are stored in the `exam_answers.csv` file for grading.

### How It Works:
1. The app first verifies the student’s identity by checking their matriculation number and name against the allowed list.
2. Once validated, students fill out the exam form, answering multiple-choice and open-ended questions.
3. After completing the exam, students can submit their answers, which will be stored in a CSV file for later grading.

## Grading Python Script

The `grading.py` script processes the answers provided by the students and calculates their scores based on both multiple-choice and open-ended questions. 

### Features:
- **Load Exam Data**: The script loads the correct answers from the `exam_solution.csv` file and student submissions from `exam_answers.csv`.
- **Multiple-Choice Grading**: For multiple-choice questions, the script compares the student's answers with the correct answers and assigns points for correct responses.
- **Open-Ended Grading**: For open-ended questions, the script calculates a similarity score using the **TF-IDF Vectorizer** and **Cosine Similarity**. Full points are given for high similarity, and partial points are awarded for moderate similarity.
- **Final Scores and Grades**: The script calculates the total score, percentage, and assigns a numerical grade based on the percentage.
- **Output**: The final results (score, percentage, numerical grade) are saved to `exam_grade_results.csv`.

### How It Works:
1. The script reads the exam answers and the correct answers.
2. It calculates the score for each student based on their answers.
3. The numerical grade is assigned using a scale based on the student's percentage.
4. The results are saved to a CSV file for review.

## Running the Application

To run this app on your local machine, follow these steps:

### Prerequisites:
- Python 3.x installed
- Streamlit library installed

### Steps:

1. Clone the repository or download the app files to your local system.
   
   ```bash
   git clone <repository_url>

2. Install Streamlit (if not already installed):

   ```bash
   pip install streamlit

3. Run the Streamlit app:
   
   ```bash
   streamlit run streamlit_app.py

4. Open the app in your browser by navigating to the provided URL (usually http://localhost:8501).

## Contributions
Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or bugs, please open an issue on the repository.

## License
This project is licensed under the MIT License.

This README explains the app, installation instructions, usage, and the file structure. Let me know if you need any adjustments!
