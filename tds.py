import streamlit as st

def largest(a, b, c):
    ans = max(a, b, c)
    return ans

st.title("Find the largest among three numbers")
st.write("Enter three numbers below:")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find the largest number"):
    f_ans = largest(num1,num2,num3)
    st.write("The largest number is:", f_ans)
