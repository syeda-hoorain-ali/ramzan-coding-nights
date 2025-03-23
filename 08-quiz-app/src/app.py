import time
import streamlit as st
from style import styles
from questions import questions
from utils import generate_question, get_feedback_message

st.set_page_config(
    page_icon="🐍",
    layout="centered",
    page_title="Python - Syeda Hoorain Ali"
)


if "questions" not in st.session_state:
    st.session_state.questions = questions.copy()

if "current_question" not in st.session_state:
    generate_question()

if "score" not in st.session_state:
    st.session_state.score = 0


curr_question: dict[str, str | list[str]] | None = st.session_state.current_question
questions_completed = (len(questions) - len(st.session_state.questions))

st.write(f"<span class='questions'>{questions_completed} / {len(questions)}</span>", unsafe_allow_html=True)
st.title("🐍 Python Quiz", anchor="heading")

container = st.container(key="container")

with container:

    if curr_question:
        st.subheader(curr_question["question"], anchor="question")
        user_choice = st.radio("answer", curr_question["options"], label_visibility="collapsed")
        if st.button("Submit answer", type="primary", key="submit-button"):

            with st.spinner("Loading..."):
                if user_choice == curr_question["answer"]:
                    st.success(f"✔ Correct answer")
                    st.session_state.score += 1
                else:
                    st.error(f'❌ Correct answer is: "{curr_question["answer"]}"')

                time.sleep(3)

                if st.session_state.questions:
                    generate_question()
                    st.rerun()

                st.session_state.current_question = None
                st.rerun()
    else:

        score: int = st.session_state.score
        
        st.subheader("Congratulations! You have completed the quiz.")
        st.subheader(f"Your score is {score} out of {len(questions)}.")
        st.subheader(get_feedback_message(score, len(questions)))

        st.balloons()


st.markdown(styles, unsafe_allow_html=True)


footer = st.container(key="footer")
footer.write("Made with 💖 by Syeda Hoorain Ali")
