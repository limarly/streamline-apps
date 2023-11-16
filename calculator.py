import streamlit as st

st.title(":bar_chart: Calculator")

#input 1
num1 = st.number_input(label="Enter the first number:",
                       step=1, value=7)

#input 2
num2 = st.number_input(label="Enter second number:",
                       step=1, value=2)

calc_options = [":heavy_plus_sign:",
                ":heavy_minus_sign:",
                ":heavy_multiplication_x:",
                ":heavy_division_sign:"]

select_option = st.radio("Select an operation to perform",
                      (calc_options))
def calculate():
    if select_option == ":heavy_plus_sign:":
        total = num1 + num2
        st.write(f"The total is {total}")
    elif select_option == ":heavy_minus_sign:":
        total = num1 - num2
        st.write(f"The total is {total}")
    elif select_option == ":heavy_multiplication_x:":
        total = num1 * num2
        st.write(f"The total is {total}")
    elif select_option == ":heavy_division_sign:" and num2 !=0:
        total = num1 / num2
        st.write(f"The total is {total}")
    else:
        st.write("The calculation is invalid")


st.button("Calculate",
          on_click=calculate
          )

