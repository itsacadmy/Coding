import streamlit as coding


coding.title("Welcome to Coding Computer Centre")
coding.header("National Computer Education Board !")
coding.subheader("Learn Web Development and Programming Languages with us in a Simple manner !")

coding.markdown("Let's Start Coding....")
coding.code("""for i in range(1,5,1)):
        print("Hello..!")
            """)
   
name=coding.text_input("Enter Your Name: ")
fname=coding.text_input("Enter Your Father's Name: ")
adr = coding.text_area("Enter Your Address: ")

classdata = coding.selectbox("Enter Your class : ",(1,2,3,4,5,6))

button = coding.button("Submit")

if button:
    coding.markdown(f"""
    Name : {name}
    Father Name: {fname}
    Address : {adr}
    Class : {classdata}
    """)
