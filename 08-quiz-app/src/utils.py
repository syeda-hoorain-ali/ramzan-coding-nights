import streamlit as st
import random


def generate_question():
    question = random.choice(st.session_state.questions)
    index = st.session_state.questions.index(question)
    st.session_state.questions.pop(index)
    st.session_state.current_question = question



def get_feedback_message(score: int, total_points: int) -> str:
    """
    Generate a feedback message based on the user's score.

    Args:
        score (int): The score obtained by the user.
        total_points (int): The total points possible.

    Returns:
        str: A feedback message.
    """

    if score == total_points:
        return "Excellent! You got everything right!"
    
    if score >= total_points * 0.75:
        return "Great job! You scored really well."
    
    if score >= total_points * 0.5:
        return "Good effort! You got more than half right."
    
    if score > 0:
        return "Keep trying! Practice makes perfect."
    
    return "Oops! Better luck next time."