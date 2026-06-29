import streamlit as st
st.title("Password Analyser")
password = st.text_input("Enter the password", type="password")
if st.button("Validate"):
    upper = lower = digit = special = False
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if len(password) >= 8 and upper and lower and digit and special:
        st.success("Strong Password")
    else:
        st.error("Invalid Password")
        if not upper:
            st.write("uppercase required")
        if not lower:
            st.write("lowercase required")
        if not digit:
             st.write("digit required ")
        if not special:
             st.write("special charecter required")
        if len(password)<8:
             st.write("length should be 8 charecters")
 
        