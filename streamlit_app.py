import streamlit as st
from datetime import datetime
import csv

# Allowed Matriculation Numbers with corresponding names (case-insensitive comparison)
allowed_matriculation_numbers = {
    "123456": "Leona Hoxha",
    "234567": "Leona Hasani",
    "345678": "Nanmanat Disayakamonpan"
}

# Title
st.title("Data Analytics Exam")
st.write("Duration: 2 hours | Total Marks: 100")

# Initialize session state variables
if "valid_matriculation" not in st.session_state:
    st.session_state.valid_matriculation = False
if "page" not in st.session_state:
    st.session_state.page = "Student Information"
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Student Information Page
if st.session_state.page == "Student Information":
    st.write("### Student Information")
    first_last_name = st.text_input("First and Last Name:", key="first_last_name_input")
    matriculation_nr = st.text_input("Matriculation Nr.:", key="matriculation_nr_input")

    # Validation
    if matriculation_nr and matriculation_nr not in allowed_matriculation_numbers:
        st.warning("Invalid Matriculation Number! Please enter a valid matriculation number to proceed.")
    elif matriculation_nr and first_last_name.strip().lower() != allowed_matriculation_numbers.get(matriculation_nr, "").lower():
        st.warning("The name and matriculation number do not match our records.")
    elif matriculation_nr in allowed_matriculation_numbers and first_last_name.strip().lower() == allowed_matriculation_numbers[matriculation_nr].lower():
        st.session_state.valid_matriculation = True
        st.session_state.page = "Exam Questions"
        st.session_state.first_last_name = first_last_name
        st.session_state.matriculation_nr = matriculation_nr
        st.success("Validation successful! Proceeding to the exam.")

# Exam Questions Page
if st.session_state.page == "Exam Questions" and st.session_state.valid_matriculation:
    # Combine all questions into one session
    exam_questions = [
        {"type": "text", "question": "What is the primary goal of data analytics?"},
        {"type": "true_false", "question": "True or False: Data visualization is not a part of data analytics."},
        {"type": "multiple_choice", "question": "Which of the following is a method for analyzing text data?", 
         "options": ["A) Clustering", "B) Regression", "C) Text Analytics", "D) None of the above"]},
        
        {"type": "text", "question": "Define 'Big Data' in your own words."},
        {"type": "multiple_choice", "question": "Which of the following is not a data type discussed in the course?",
         "options": ["A) Temporal Data", "B) Geospatial Data", "C) Quantum Data", "D) Multidimensional Data"]},
        
        {"type": "text", "question": "Explain the importance of visual encoding in data analytics."},
        {"type": "multiple_choice", "question": "Which R command is used for logistic regression?",
         "options": ["A) lm", "B) glm", "C) plot", "D) summary"]},
        
        {"type": "text", "question": "Describe a real-world application of clustering."},
        {"type": "true_false", "question": "True or False: Supervised learning requires labeled data."},
        
        {"type": "text", "question": "What is the bias-variance trade-off?"},
        {"type": "multiple_choice", "question": "Which of the following is a statistical learning method?",
         "options": ["A) Decision Trees", "B) Neural Networks", "C) Both A and B", "D) None of the above"]},
        
        {"type": "text", "question": "List the steps involved in EDA."},
        {"type": "true_false", "question": "True or False: EDA is a one-time process."},
        
        {"type": "text", "question": "What are the key components of the data science cycle?"},
        {"type": "multiple_choice", "question": "Which of the following is not part of the data science cycle?",
         "options": ["A) Data Collection", "B) Data Cleaning", "C) Data Ignoring", "D) Data Analysis"]},
        
        {"type": "text", "question": "Explain the concept of predictive modeling."},
        {"type": "true_false", "question": "True or False: Predictive modeling can be used for forecasting future events."},
        
        {"type": "text", "question": "What is the purpose of data transformation in analytics?"},
        {"type": "multiple_choice", "question": "Which of the following is a data aggregation technique?",
         "options": ["A) Summarization", "B) Visualization", "C) Encoding", "D) None of the above"]},
        
        {"type": "text", "question": "Describe the process of text analytics."},
        {"type": "true_false", "question": "True or False: Document analytics is only applicable to digital documents."},
        
        {"type": "text", "question": "What are some challenges faced in data analytics?"},
        {"type": "multiple_choice", "question": "Which of the following is an advanced data analytics technique?",
         "options": ["A) Simple Regression", "B) Neural Networks", "C) Basic Clustering", "D) None of the above"]},
    ]

    # Display questions and collect answers
    answers = {}
    for i, question_data in enumerate(exam_questions, start=1):
        q_type = question_data["type"]
        question = question_data["question"]
        key = f"question_{i}"  # Unique key for each question

        if q_type == "text":
            answer = st.text_area(question, key=key, placeholder="Enter your answer here")
        elif q_type == "true_false":
            # Using None for the default to prevent pre-selection
            answer = st.radio(question, ["True", "False"], key=key, index=None)
        elif q_type == "multiple_choice":
            # Using None for the default to prevent pre-selection
            answer = st.radio(question, question_data["options"], key=key, index=None)
        else:
            answer = ""

        answers[question] = answer

    # Save answers to session state
    st.session_state.answers["All Questions"] = answers

    if st.button("Submit Exam"):
        submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Prepare the data for a single row per student
        student_data = {
            "Name": st.session_state.first_last_name,
            "Matriculation Number": st.session_state.matriculation_nr,
            "Submission Time": submission_time
        }

        # Add all answers to the student data dictionary
        for question, answer in answers.items():
            student_data[question] = answer

        # Save to CSV (appending to a file)
        try:
            with open("exam_answers.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=student_data.keys())
                
                # Write header only if file is empty
                if f.tell() == 0:
                    writer.writeheader()

                writer.writerow(student_data)
                
            st.success("Exam submitted successfully!")
        except Exception as e:
            st.error(f"An error occurred while saving your answers: {e}")
