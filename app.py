from dotenv import load_dotenv
load_dotenv() ## load all the environment variables
import os
import streamlit as st
import sqlite3


import google.generativeai as genai
## configuer the google credentials
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()
for model in models:
    print(model.name)

##function to load google gemini model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest') 
    response = model.generate_content([prompt[0],question])
    return response.text

##function to retrieve the query from the database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## defining the prompt

prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION \n\nFor example, \nExample 1 - How many entries of records are present?,the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science Class ?,the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
    also the sql code should not ''' in begining or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ",key="input")

submit = st.button("Ask me question")

## if submit is clicked

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)