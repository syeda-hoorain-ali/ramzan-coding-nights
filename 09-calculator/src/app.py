import streamlit as st
from style import styles
from streamlit_grid import streamlit_grid, GridItem


st.set_page_config(
    page_icon=":material/calculate:",
    layout="centered",
    page_title="Calculator - Syeda Hoorain Ali"
)


if "equation" not in st.session_state:
    st.session_state.equation = '0'

if "last_value" not in st.session_state:
    st.session_state.last_value = None  # Store the last clicked button to avoid multiple reruns



st.success(st.session_state.equation)
st.markdown(styles, True)

grid = [
    [GridItem("C", col_span=2, background_color="red", text_color="white"), GridItem("/"), GridItem("*")],
    [GridItem("7"), GridItem("8"), GridItem("9"), GridItem("-")],
    [GridItem("4"), GridItem("5"), GridItem("6"), GridItem("+", row_span=2)],
    [GridItem("1"), GridItem("2"), GridItem("3")],
    [GridItem("0"), GridItem("00"), GridItem("."), GridItem("=", background_color="#2B90DE", text_color="white")],
]

selected_value = streamlit_grid(
    grid_layout=grid, 
    columns=4, 
    gap=10, 
    cell_height=15,
    background_color="#5e528a",
    use_container_width=True
)


if selected_value != st.session_state.last_value:
    st.session_state.last_value = selected_value

    # Clear Equation
    if selected_value == 'C':
        st.session_state.equation = '0'


    # Handle Digits
    elif selected_value.isdigit():

        if st.session_state.equation in ['0', 'Error']:
            st.session_state.equation = selected_value

        else:
            st.session_state.equation += selected_value


    # Handle Operators
    elif selected_value in ['+', '-', '*', '/']:

        if st.session_state.equation[-1] not in ['+', '-', '*', '/']:
            st.session_state.equation += f" {selected_value} "
        
        else:
            # Replace last operator with new one
            st.session_state.equation = st.session_state.equation[:-1] + f" {selected_value} "


    # Handle Decimal Point
    elif selected_value == '.':

        numbers: list[str] = st.session_state.equation.split(" ")
        last_number = numbers[-1]
        print(numbers)

        if '.' not in last_number:
            st.session_state.equation += selected_value


    # Handle Equals
    if selected_value == '=':
        try:
            st.session_state.equation = str(eval(st.session_state.equation))
        except Exception as e:
            print(e)
            st.session_state.equation = 'Error'


    st.rerun()

