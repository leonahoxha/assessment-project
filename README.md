# Data Analytics Exam Streamlit App

## Overview

This Streamlit app is designed to simulate an online exam for data analytics students. It allows candidates to enter their information, such as their name and matriculation number, and then proceed to answer multiple-choice and open-ended questions. The responses are stored in a single text file for evaluation purposes.

## Features

- **Candidate Information Page:** 
  - Collects the candidate’s first and last name and matriculation number.
  - Checks if the matriculation number is valid from a predefined list.
  
- **Exam Questions Page:**
  - Once valid candidate information is entered, the user is redirected to the exam questions page.
  - The exam consists of multiple sections:
    - **Section A:** Short answer questions (10 questions, 4 marks each)
    - **Section B:** Problem-solving and application (4 questions, 10 marks each)
    - **Section C:** Essay question (choose one of two topics, 20 marks)
  
- **Submit Exam:**
  - The candidate can submit the exam answers after completing all sections.
  - All answers, along with candidate information, are saved in a single file (`exam_answers.txt`), which can be reviewed later.

## Installation

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

## Usage

### Start the App:
- Upon launching, candidates are prompted to enter their first and last name and matriculation number.

### Proceed to Exam:
- After entering the candidate’s information, the user clicks on the **"Proceed to Exam"** button to access the exam questions.

### Answer the Questions:
- The candidate answers the questions in three sections:
  - **Section A:** Short Answer
  - **Section B:** Problem-Solving and Application
  - **Section C:** Essay

### Submit the Exam:
- After completing the exam, candidates can submit their answers. The responses are saved to a text file called `exam_answers.txt`.

## File Structure
- `streamlit_app.py`: The main Streamlit app file where the logic of the app is implemented.
- `exam_answers.txt`: The text file where all exam responses are stored.

## Contributions
Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or bugs, please open an issue on the repository.

## License
This project is licensed under the MIT License.

This README explains the app, installation instructions, usage, and the file structure. Let me know if you need any adjustments!
