import streamlit as st
import joblib
st.title('Loan Approval Process Automation')
model=joblib.load('loan_data1.joblib')
Gender=st.number_input('enter the gender Male:0 Female:1')
Married=st.number_input('enter  martial status unmarried:0 married:1')
Income=st.number_input('Loan ammount in thousands')
if st.button('predict Approval'):
    predictions=model.predict([[Gender,Married,Income,la]])
    if predictions=='y':
        st.text('Loan Approval')
    else:
        st.text('Loan Rejected')
