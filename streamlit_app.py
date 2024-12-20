import streamlit as st
from datetime import datetime

# Allowed Matriculation Numbers
allowed_matriculation_numbers = ["123456", "654321", "112233", "445566"]

# Title
st.title("Data Analytics Exam")
st.write("Duration: 2 hours | Total Marks: 100")

# Initialize session state variables for matriculation number and name
if 'valid_matriculation' not in st.session_state:
    st.session_state.valid_matriculation = False
if 'first_last_name' not in st.session_state:
    st.session_state.first_last_name = ""
if 'matriculation_nr' not in st.session_state:
    st.session_state.matriculation_nr = ""
if 'page' not in st.session_state:
    st.session_state.page = "Candidate Information"  # Default page is Candidate Information

# Create navigation for pages
if st.session_state.page == "Candidate Information":
    st.radio("Navigate", ["Candidate Information", "Exam Questions"], index=0, key="navigation", disabled=True)
elif st.session_state.page == "Exam Questions":
    st.radio("Navigate", ["Candidate Information", "Exam Questions"], index=1, key="navigation", disabled=True)

# Candidate Information Page
if st.session_state.page == "Candidate Information":
    st.write("### Candidate Information")
    
    # Get Candidate Information
    first_last_name = st.text_input("First and Last Name:", key="first_last_name_input")
    matriculation_nr = st.text_input("Matriculation Nr.:", key="matriculation_nr_input")
    
    # Check Matriculation Number
    if matriculation_nr and matriculation_nr not in allowed_matriculation_numbers:
        st.warning("Invalid Matriculation Number! Please enter a valid matriculation number to proceed.")
    
    # Proceed button that updates session state if valid
    if matriculation_nr in allowed_matriculation_numbers and first_last_name:
        if st.button("Proceed to Exam (Press Twice)"):
            # Save to session state and move to the next page (Exam Questions)
            st.session_state.first_last_name = first_last_name
            st.session_state.matriculation_nr = matriculation_nr
            st.session_state.valid_matriculation = True
            st.session_state.page = "Exam Questions"  # Update the page to Exam Questions

# Exam Questions Page
elif st.session_state.page == "Exam Questions":
    if not st.session_state.valid_matriculation:
        st.error("You must provide valid candidate information first!")
    else:
        # Section A: Short Answer Questions
        st.write("### Section A: Short Answer Questions (10 x 4 = 40 Marks)")
        st.write("Answer the following questions concisely. Each question carries 4 marks.")
        
        questions_a = [
            "Define Big Data and explain how it differs from traditional data.",
            "List and describe the main categories in a taxonomy of data types.",
            "Explain the concept of Visual Analytics and its role in data exploration.",
            "What are the key differences between supervised and unsupervised learning?",
            "Define clustering and provide an example of its application.",
            "Briefly describe two visualization techniques used for multidimensional data.",
            "What is the purpose of outlier detection in data analysis?",
            "Give an example of how text and document analytics can be applied in a business context.",
            "Explain the importance of understanding data relationships in analytics.",
            "Why is it important to assess the performance of an analytics method?",
        ]

        answers_a = []
        for i, question in enumerate(questions_a, 1):
            st.write(f"{i}. {question}")
            answer = st.text_input(f"Answer {i}:")
            answers_a.append(answer)
        
        # Section B: Problem-Solving and Application
        st.write("### Section B: Problem-Solving and Application (4 x 10 = 40 Marks)")
        st.write("Solve the following problems or apply your knowledge to practical scenarios. Each question carries 10 marks.")
        
        questions_b = [
            "Taxonomy of Data Types: A dataset contains the following attributes: Age (years), Income (USD), Gender (Male/Female), Product Rating (1-5 stars), Purchase Date (timestamp). Classify each attribute into an appropriate data type (e.g., categorical, ordinal, etc.) and justify your classification.",
            "Clustering Application: You are working on customer segmentation for an e-commerce company. Explain how clustering could help the company and describe the steps you would take to perform the clustering.",
            "Text Analytics: A dataset contains thousands of customer reviews for a product. Suggest a method for analyzing this data to determine customer sentiment and provide a step-by-step approach.",
            "Supervised Learning Evaluation: A logistic regression model was trained to classify emails as spam or not spam. The confusion matrix is as follows: Predicted Spam | Predicted Not Spam; Actual Spam | 50 | 10; Actual Not Spam | 20 | 70. Calculate the following metrics and interpret them: Precision, Recall, Accuracy."
        ]

        answers_b = []
        for i, question in enumerate(questions_b, 1):
            st.write(f"{i}. {question}")
            answer = st.text_area(f"Answer {i}:")
            answers_b.append(answer)

        # Section C: Essay Question
        st.write("### Section C: Essay Question (20 Marks)")
        st.write("Choose one of the following topics and write an essay (approx. 300 words).")

        essay_topics = [
            "Importance of Data Visualization: Discuss how data visualization aids in analytical reasoning and decision-making. Include examples of different visualization techniques and their applications.",
            "Temporal Data Analytics: Explain the challenges and methods for analyzing temporal data. Provide examples of real-world applications and discuss how insights derived from temporal data can drive decisions.",
        ]

        answers_c = []
        for i, topic in enumerate(essay_topics, 1):
            st.write(f"{i}. {topic}")
            answer = st.text_area(f"Essay {i}:")
            answers_c.append(answer)

        # Submit Button and Save to One File
        if st.button("Submit Exam"):
            if st.session_state.matriculation_nr not in allowed_matriculation_numbers:
                st.error("Your Matriculation Number is not authorized to submit the exam.")
            else:
                submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("exam_answers.txt", "a") as f:
                    f.write("========================================\n")
                    f.write(f"Submission Time: {submission_time}\n")
                    f.write(f"First and Last Name: {st.session_state.first_last_name}\n")
                    f.write(f"Matriculation Nr.: {st.session_state.matriculation_nr}\n\n")
                    f.write("Section A: Short Answer Questions\n")
                    for i, answer in enumerate(answers_a, 1):
                        f.write(f"Q{i}: {answer}\n")
                    f.write("\nSection B: Problem-Solving and Application\n")
                    for i, answer in enumerate(answers_b, 1):
                        f.write(f"Q{i}: {answer}\n")
                    f.write("\nSection C: Essay Question\n")
                    for i, answer in enumerate(answers_c, 1):
                        f.write(f"Essay {i}: {answer}\n")
                    f.write("========================================\n\n")
                st.success("Your answers have been submitted and saved.")
