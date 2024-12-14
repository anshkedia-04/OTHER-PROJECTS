import streamlit as st
import random
import time

# Title and Description
st.title("🔢 Fun Math Game")
st.write("Test your math skills by solving dynamic arithmetic problems!")

# Sidebar for Game Settings
st.sidebar.header("Game Settings")

game_mode = st.sidebar.selectbox("Select Game Mode:", ["Timed Mode", "Challenge Mode"])
difficulty = st.sidebar.selectbox("Select Difficulty:", ["Easy", "Medium", "Hard"])
num_questions = st.sidebar.number_input(
    "Number of Questions (For Challenge Mode):", min_value=5, max_value=50, value=10, step=1
)
time_limit = st.sidebar.slider(
    "Time Limit per Question (Seconds):", min_value=5, max_value=30, value=10
)

# Helper Functions
def generate_problem(difficulty):
    """Generate a random arithmetic problem based on the selected difficulty."""
    if difficulty == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "Medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
    else:  # Hard
        a, b = random.randint(50, 100), random.randint(50, 100)

    operation = random.choice(["+", "-", "*", "/"])
    if operation == "/":
        b = random.randint(1, 10)  # Avoid complex division for simplicity
    return a, b, operation

def calculate_answer(a, b, operation):
    """Calculate the answer for the given arithmetic problem."""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return round(a / b, 2)

# Game Variables
score = 0
correct_answers = 0
total_questions = 0
start_game = st.button("Start Game")

if start_game:
    if game_mode == "Timed Mode":
        st.write(f"You have {time_limit} seconds per question. Try to score as much as you can!")
        end_time = time.time() + time_limit * num_questions

        while time.time() < end_time:
            a, b, operation = generate_problem(difficulty)
            correct_answer = calculate_answer(a, b, operation)

            user_answer = st.text_input(f"Solve: {a} {operation} {b}")

            if user_answer:
                try:
                    user_answer = float(user_answer)
                    if user_answer == correct_answer:
                        st.success("Correct!")
                        score += 1
                        correct_answers += 1
                    else:
                        st.error(f"Wrong! The correct answer was {correct_answer}")
                except ValueError:
                    st.error("Please enter a valid number.")

                total_questions += 1
                st.text_input("Next Question", key=f"next{total_questions}")
    
    elif game_mode == "Challenge Mode":
        st.write(f"Solve {num_questions} questions as fast as you can!")
        start_time = time.time()

        for _ in range(num_questions):
            a, b, operation = generate_problem(difficulty)
            correct_answer = calculate_answer(a, b, operation)

            user_answer = st.text_input(f"Solve: {a} {operation} {b}")

            if user_answer:
                try:
                    user_answer = float(user_answer)
                    if user_answer == correct_answer:
                        st.success("Correct!")
                        score += 1
                        correct_answers += 1
                    else:
                        st.error(f"Wrong! The correct answer was {correct_answer}")
                except ValueError:
                    st.error("Please enter a valid number.")

                total_questions += 1
                st.text_input("Next Question", key=f"next{total_questions}")

        end_time = time.time()
        st.write(f"You completed the challenge in {round(end_time - start_time, 2)} seconds!")

# Results
if total_questions > 0:
    st.write("## Game Results")
    st.write(f"Score: {score}")
    st.write(f"Correct Answers: {correct_answers}/{total_questions}")
    accuracy = (correct_answers / total_questions) * 100
    st.write(f"Accuracy: {accuracy:.2f}%")

    if game_mode == "Challenge Mode":
        st.write(f"Time Taken: {round(end_time - start_time, 2)} seconds")
