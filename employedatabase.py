import streamlit as st

st.set_page_config(layout='wide')



menu = ['Register Staff','Staff Database','Staff File']
choose = st.sidebar.selectbox('Menu',menu)





if choose == 'Register Staff':

    st.title("Register Here")
    
    fn1,fn2 = st.columns(2)


    with fn1:
        first = st.text_input("First Name")
    with fn2:
        last = st.text_input("Last Name")

    ea1,ea2 = st.columns(2)

    with ea1:
        adress = st.text_input("Email Adress")
    with ea2:
        gender = st.radio('Gender',['Male','Female'],horizontal=True)

   
    department = st.selectbox('Department',['Management','Accounting ','Engineering','Human Resources','Security','Medical','Transportation'])

    jobtitle = st.selectbox('Job Title',['Board of Directors','Supervisor','senior staff','junior staff','paid entern','unpaid entern'])

    cont1,cont2 = st.columns(2)

    with cont1:
        status = st.selectbox('Contract_status',['Full time','Part time'])

    with cont2:
        income = st.number_input('Monthly income',0)

    
    degree = st.selectbox('Educational degree',['None','Associate degree','Bachelor degree','Gradute degree','Professional degree','Doctoral degree'])

    
    date = st.date_input('Employement date')

    but1,but2 = st.columns(2)

    with but1:
     if st.button("Submit Employe data"):
       st.success(f"You have submited we will get back to you shortly")
