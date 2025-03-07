import streamlit as st
from units import unit_converter, unit_dict
from style import styles

st.set_page_config(
    page_icon="assets/logo.png",
    layout="centered",
    page_title="Unit Converter - Syeda Hoorain Ali"
)

 
st.logo("assets/logo.png", size="large")
st.markdown(styles, unsafe_allow_html=True)
st.header("✨ Unit Converter ✨")


def display_conversion_ui(category: str):
    options: list[str] = [key.capitalize() for key in unit_dict[category].keys()]
    col1, col2 = st.columns(2)
    col3, = st.columns(1)

    from_unit = col1.selectbox("From", options)
    to_unit = col2.selectbox("To", options)
    
    from_value = col3.number_input("Value", key="value", min_value=0.0)
    converted_value = unit_converter(from_value, from_unit, to_unit, category)
    
    col, = st.columns(1) #* caution: in case of removing comma try `col[0]` with indexing 
    col.success(f"Converting {round(from_value, 2)} {from_unit} to {converted_value} {to_unit}", icon="✅")



container = st.container(key="container")

with container:
    col, = st.columns(1) #* caution: in case of removing comma try `col[0]` with indexing 
    category = col.selectbox("Category", list(unit_dict.keys()), label_visibility="collapsed")
    display_conversion_ui(category)



#^ You can also try tabs method 
#& Don't forgot to comment column method before uncommenting this
# tabs =  container.tabs(list(unit_dict.keys()))
# for i, tab in enumerate(tabs):
#     category = list(unit_dict.keys())[i]
#     with tab:
#         display_conversion_ui(category)



footer = st.container(key="footer")
footer.write("Made with 💖 by Syeda Hoorain Ali")
